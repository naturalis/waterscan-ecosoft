from flask_restful import Resource
from services.MapService import MapService

# @author: Wim van der Putten
class MapResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return MapService.getMarkersByFilter(self)


