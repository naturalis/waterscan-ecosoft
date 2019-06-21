from flask_restful import Resource
from services.ReferenceService import ReferenceService

class ReferenceResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return ReferenceService.getReference(self, id)

class ReferencesResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return ReferenceService.getAllReferences(self)

class ReferenceByWatertypeResource(Resource):
    def get(self, watertype_id):
        """GET request for this resource layer passes it to service layer"""
        return ReferenceService.getReferenceWatertype(self, watertype_id)