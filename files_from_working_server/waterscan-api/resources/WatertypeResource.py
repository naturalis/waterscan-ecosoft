from flask_restful import Resource
from services.WatertypeService import WatertypeService

class WatertypeResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return WatertypeService.getWaterType(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return WatertypeService.updateWaterType(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return WatertypeService.addWaterType(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return WatertypeService.removeWatertype(self, id)

class WatertypesResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return WatertypeService.getAllWatertypes(self)