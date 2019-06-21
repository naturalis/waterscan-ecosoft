from flask_restful import Resource
from services.WaterschapService import WaterschapService

class WaterschapResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return WaterschapService.getWaterschap(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return WaterschapService.updateWaterschap(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return WaterschapService.removeWaterschap(self, id)

class WaterschappenResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return WaterschapService.getAllWaterschappen(self)

    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return WaterschapService.addWaterschap(self)