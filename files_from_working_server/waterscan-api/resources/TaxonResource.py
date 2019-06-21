from flask_restful import Resource
from services.TaxonService import TaxonService

class TaxonResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return TaxonService.getTaxon(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return TaxonService.updateTaxon(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return TaxonService.addTaxon(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return TaxonService.removeTaxon(self, id)

class TaxonsResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return TaxonService.getAllTaxons(self)

class TaxonByIdsResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return TaxonService.getTaxonByIds(self)

class TaxonFindResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return TaxonService.findOrCreate(self)

class TaxonFamilyResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return TaxonService.getFamily(self, id)

class TaxonUpdateResource(Resource):
    def put(self, taxonIds):
        """PUT request for this resource layer passes it to service layer"""
        pass 