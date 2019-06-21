from flask_restful import Resource
from services.TaxonLevelService import TaxonLevelService

class TaxonLevelResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return TaxonLevelService.getTaxonLevel(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return TaxonLevelService.updateTaxonLevel(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return TaxonLevelService.addTaxonLevel(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return TaxonLevelService.removeTaxonLevel(self, id)

class TaxonLevelsResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return TaxonLevelService.getAllTaxonLevels(self)