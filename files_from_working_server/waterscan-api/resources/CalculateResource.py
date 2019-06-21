from flask_restful import Resource, reqparse
from services.CalculateService import CalculateService

class CalculateResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return CalculateService.getSampleById(self, id)

class CalulateReferenceResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return CalculateService.getReferenceById(self, id)


