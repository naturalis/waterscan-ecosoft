from models.TaxonGroup import TaxonGroup
from flask_restful import reqparse
from flask import request
from sqlalchemy import exc
from services.AuthService import AuthService

# This service contains the functionality of the GET, PUT, POST, and DELETE calls for TaxonGroup
class TaxonGroupService:
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="ID cannot be left blank!")
    parser.add_argument("code", type=str, required=True, help="Code cannot be left blank!")
    parser.add_argument("description", type=str, required=True, help="Description cannot be left blank!")
    parser.add_argument("icon", type=str, required=True, help="Icon cannot be left blank!")

    # This method fetches a Taxongroup from the database
    @AuthService.tokenRequired
    def getTaxonGroup(self, id):
        taxon = TaxonGroup.findTaxonGroupById(id)
        if taxon:
            return taxon.json(), 201
        return {"message": "The taxongroup is not found!"}, 404

    # This method creates or updates a taxongroup
    @AuthService.adminRequired
    def updateTaxonGroup(self, id):
        try:
            data = TaxonGroupService.parser.parse_args()
            taxongroup = TaxonGroup.findTaxonGroupById(id)

            if taxongroup:
                taxongroup.code = data["code"]
                taxongroup.description = data["description"]
                taxongroup.icon = data["icon"]
            else:
                taxongroup = TaxonGroup(data["id"], data["code"], data["description"], data["icon"])

            taxongroup.save()
            return taxongroup.json()
        except exc.IntegrityError:
            return "The Code already exists!"

    # This method creates, and only creates a taxongroup.
    @AuthService.adminRequired
    def addTaxonGroup(self, id):
        try:
            data = TaxonGroupService.parser.parse_args()
            taxongroup = TaxonGroup.findTaxonGroupById(id)

            if taxongroup:
                return "The Taxongroup already exists!"
            else:
                taxongroup = TaxonGroup(data["id"], data["code"], data["description"], data["icon"])
                taxongroup.save()
                return taxongroup.json()
        except exc.IntegrityError:
            return "The code already exists!"

    # This method removes a taxongroup from the database.
    @AuthService.adminRequired
    def removeTaxonGroup(self, id):
        taxongroup = TaxonGroup.findTaxonGroupById(id)
        if taxongroup:
            taxongroup.delete()
            return {"message": "The taxongroup with id '{}' is deleted!".format(id)}
        else:
            return "The taxongroup does not exist!"

    @AuthService.tokenRequired
    def getAllTaxonGroups(self):
        return list(map(lambda x: x.json(), TaxonGroup.findAllTaxonGroups()))