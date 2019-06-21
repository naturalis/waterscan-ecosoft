from flask_restful import Resource
from services.TaxonGroupService import TaxonGroupService

class TaxonGroupResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return TaxonGroupService.getTaxonGroup(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return TaxonGroupService.updateTaxonGroup(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return TaxonGroupService.addTaxonGroup(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return TaxonGroupService.removeTaxonGroup(self, id)

class TaxonGroupsResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return TaxonGroupService.getAllTaxonGroups(self)
