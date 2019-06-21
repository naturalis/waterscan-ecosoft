from flask_restful import Resource
from services.ReferenceTaxonService import ReferenceTaxonService

class ReferenceTaxonResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return ReferenceTaxonService.addTaxon(self)

class ReferencetaxonResourceValue(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return ReferenceTaxonService.getReference(self, id)
