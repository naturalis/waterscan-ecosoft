from flask_restful import Resource
from services.LocationService import LocationService

class LocationResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return LocationService.getLocation(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return LocationService.updateLocation(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return LocationService.addLocation(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return LocationService.removeLocation(self, id)

class LocationByCodeResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return LocationService.getLocationByCode(self)

class LocationsResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return LocationService.getAllLocations(self)

class LocationByIds(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return LocationService.getLocationByIds(self)
