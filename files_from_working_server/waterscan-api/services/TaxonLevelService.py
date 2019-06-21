from models.TaxonLevel import TaxonLevel
from flask_restful import reqparse
from flask import request
from sqlalchemy import exc
from services.AuthService import AuthService

class TaxonLevelService:
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Name cannot be left blank!")

    # This method fetches the Taxon Level from the database.
    @AuthService.tokenRequired
    def getTaxonLevel(self, id):
        taxonlevel = TaxonLevel.findTaxonLevelById(id)
        if taxonlevel:
            return taxonlevel.json(), 201
        return {"message": "The taxon level is not found in the database."}, 404

    # This method creates or updates the given Taxon Level.
    @AuthService.tokenRequired
    def getAllTaxonLevels(self):
        return list(map(lambda x: x.json(), TaxonLevel.findAllTaxonLevels()))

    @AuthService.tokenRequired
    def updateTaxonLevel(self, id):
        try:
            data = TaxonLevelService.parser.parse_args()
            taxonlevel = TaxonLevel.findTaxonLevelById(id)
            if taxonlevel:
                taxonlevel.name = data["name"]
            else:
                taxonlevel = TaxonLevel(data["name"])

            taxonlevel.save()
            return taxonlevel.json()
        except exc.IntegrityError:
            return "The name already exists!"

    # This method creates, and only creates a Taxon Level.
        taxonlevel.save()
        return taxonlevel.json()

    @AuthService.adminRequired
    def addTaxonLevel(self, id):
        try:
            data = TaxonLevelService.parser.parse_args()
            taxonlevel = TaxonLevel.findTaxonLevelById(id)

            if taxonlevel:
                return "The Taxonlevel already exists!"
            else:
                taxonlevel = TaxonLevel(data["name"])
                taxonlevel.save()
                return taxonlevel.json()
        except exc.IntegrityError:
            return "The name already exists!"

    @AuthService.adminRequired
    def removeTaxonLevel(self, id):
        taxonlevel = TaxonLevel.findTaxonLevelById(id)
        if taxonlevel:
            taxonlevel.delete()
            return {"message": "The taxonlevel with id '{}' is deleted!".format(id)}
        else:
            return "The taxonlevel does not exist!"

    def getAllTaxonLevels(self):
        return list(map(lambda x: x.json(), TaxonLevel.findAllTaxonLevels()))