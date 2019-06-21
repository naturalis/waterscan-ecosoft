from models.ReferenceTaxon import ReferenceTaxon
from models.Reference import Reference
from flask_restful import reqparse
from flask import request
from sqlalchemy import exc
from services.AuthService import AuthService

class ReferenceTaxonService:
    parser = reqparse.RequestParser()
    parser.add_argument("taxon_id", type=int, required=True, help="Name cannot be left empty!")

#    def getReference(self, id):
    @AuthService.adminRequired
    def addTaxon(self):
        json = request.json
        for taxonID in json["taxonIds"]:
            ReferenceTaxon(json["id"], taxonID).save()
        return "Added taxons to reference"


    def getReference(self, id):
        # retrieves the list
        results = ReferenceTaxon.findTaxonListBySampleId(id)

        # create some lists
        wew_valueList = []
        taxonList = []
        newTaxonList = []

        # loop through the results
        for result in results:
            # seperate the values to their own lists
            wew_valueList.append(result.WewValue.jsonCalc())
            taxonList.append(result.Taxon)
        taxonList = list(set(taxonList));
        newTaxonList = list((map(lambda x: x.jsonSample(), taxonList)))
        result = ReferenceTaxon(id, newTaxonList, wew_valueList)
        return result.jsonValue()
