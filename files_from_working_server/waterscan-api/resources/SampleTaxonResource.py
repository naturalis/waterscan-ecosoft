from flask_restful import Resource
from services.SampleTaxonService import SampleTaxonService

# @author: Wim van der Putten
class SampleTaxonResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return SampleTaxonService.getSample(self, id)
