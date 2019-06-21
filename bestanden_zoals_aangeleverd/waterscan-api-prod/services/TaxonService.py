from models.Taxon import Taxon
from flask_restful import reqparse
from flask import request, jsonify
from sqlalchemy import exc
from services.AuthService import AuthService

# This service's task is  to get, create, update and delete specifix taxa.
class TaxonService:
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="ID cannot be left blank!")
    parser.add_argument("name", type=str, required=True, help="Name cannot be left blank!")
    parser.add_argument("group_id", type=str, required=True, help="Name cannot be left blank!")
    parser.add_argument("level_id", type=str, required=True, help="Name cannot be left blank!")
    parser.add_argument("parent_id", type=str, required=True, help="Code cannot be left blank!")
    parser.add_argument("refer_id", type=str, required=True, help="Code cannot be left blank!")

    # This method returns a specific taxon from the database.
    @AuthService.tokenRequired
    def getTaxon(self, id):
        taxon = Taxon.findTaxonById(id)
        if taxon:
            return taxon.json(), 201
        return {"message": "The taxon is not found!"}, 404

    # This method looks whether there is a taxon or not, and then updates or creates it.
    @AuthService.adminRequired
    def updateTaxon(self, id):
        try:
            data = TaxonService.parser.parse_args()
            taxon = Taxon.findTaxonById(id)

            if taxon:
                taxon.name = data["name"]
                taxon.group_id = data["group_id"]
                taxon.level_id = data["level_id"]
                taxon.parent_id = data["parent_id"]
                taxon.refer_id = data["refer_id"]
            else:
                taxon = Taxon(data["id"], data["name"], data["group_id"], data["level_id"], data["parent_id"], data["refer_id"])

            taxon.save()
            return taxon.json()
        except exc.IntegrityError:
            return "The name already exists!"

    # This method adds, and only adds a new taxon.
    @AuthService.adminRequired
    def addTaxon(self, id):
        try:
            data = TaxonService.parser.parse_args()
            taxon = Taxon.findTaxonById(id)

            if taxon:
                return "The Taxon already exists!"
            else:
                taxon = Taxon(data["id"], data["name"], data["group_id"], data["level_id"], data["parent_id"], data["refer_id"])
                taxon.save()
                return taxon.json()
        except exc.IntegrityError:
            return "The name already exists!"

    # This method removes a taxon.

    @AuthService.adminRequired
    def removeTaxon(self, id):
        taxon = Taxon.findTaxonById(id)
        if taxon:
            taxon.delete()
            return {"message": "The taxon with id '{}' is deleted!".format(id)}
        else:
            return "The taxon does not exist!"

    @AuthService.tokenRequired
    def getAllTaxons(self):
        return list(map(lambda x: x.json(), Taxon.findAllTaxons()))

    @AuthService.tokenRequired
    def getTaxonByIds(self):
        data = request.get_json(force=True)
        print(data)
        taxons = []
        for x in data:
            taxon = Taxon.findTaxonById(x)
            taxons.append(taxon)
        return list(map(lambda x: x.json(), taxons))

    def getFamily(self, id):
        # Find the parents
        # Make a list to put all the family taxa inside of
        familyList = []
        # Get the base taxon object
        base = Taxon.findTaxonById(id)
        # Add the base to the list
        familyList.append(base.json())
        taxon = base
        # While there is a taxon with a parent id
        while taxon and taxon.parent_id:
            # The parent taxon becomes the taxon, so the while loop keeps looking
            taxon = taxon.findTaxonById(taxon.parent_id)
            # Add the parent taxon to the list
            familyList.append(taxon.json())


        #Find the children of the base ID
        lookForChildren = []
        lookForChildren.append(id)

        while len(lookForChildren) > 0:
            children = Taxon.findChildrenById(lookForChildren)
            lookForChildren.clear()
            for child in children:
                lookForChildren.append(child.id)
                familyList.append(child.json())
            lookForChildren.clear()

        return familyList

    def findOrCreate(self):
        json = request.json
        taxonList = []
        for soort in json:
            taxon = Taxon.findTaxonByName(soort)
            if taxon is None:
                taxon = Taxon(name=soort)
            taxonList.append(taxon.json())
        return jsonify(taxonList)
