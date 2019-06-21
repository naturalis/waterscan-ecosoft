from models.Location import Location
from flask_restful import reqparse
from sqlalchemy import exc
from flask import request
from services.AuthService import AuthService

class LocationService:
    # A parser to catch the payload of the request
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="ID cannot be left blank!")
    parser.add_argument("code", type=str, required=True, help="Code cannot be left blank!")
    parser.add_argument("description", type=str, required=True, help="Description cannot be left blank!")
    parser.add_argument("x_coor", type=str, required=True, help="X Coordinate cannot be left blank!")
    parser.add_argument("y_coor", type=str, required=True, help="Y Coordinate cannot be left blank!")
    parser.add_argument("waterschap_id", type=str, required=True, help="Waterschap ID cannot be left blank!")
    parser.add_argument("watertype_id", type=str, required=True, help="Watertype ID cannot be left blank!")
    parser.add_argument("watertype_krw_id", type=str, required=True, help="Watertype KRW ID cannot be left blank!")

    @AuthService.tokenRequired
    def getLocation(self, id):
        """Returns JSON object of a location"""
        location = Location.findLocationById(id)
        if location:
            return location.json(), 201
        return {"message": "The location is not found in the database."}, 404

    @AuthService.tokenRequired
    def updateLocation(self, id):
        """Returns JSON object of the created or updated location"""
        try:
            data = LocationService.parser.parse_args()
            location = Location.findLocationById(id)
            if location:
                location.code = data["code"]
                location.description = data["description"]
                location.x_coor = data["x_coor"]
                location.y_coor = data["y_coor"]
                location.waterschap_id = data["waterschap_id"]
                location.watertype_id = data["watertype_id"]
                location.watertype_krw_id = data["watertype_krw_id"]
            else:
                location = Location(id, data["code"], data["description"], data["x_coor"], data["y_coor"], data["waterschap_id"], data["watertype_id"], data["watertype_krw_id"])
            location.save()
            return location.json()
        except exc.IntegrityError:
            return "The code already exists!"

    @AuthService.tokenRequired
    def addLocation(self, id):
        """Returns JSON object of the created location"""
        try:
            data = LocationService.parser.parse_args()
            location = Location.findLocationById(id)
            if location:
                return "The location already exists!"
            else:
                location = Location(id, data["code"], data["description"], data["x_coor"], data["y_coor"], data["waterschap_id"], data["watertype_id"], data["watertype_krw_id"])
                location.save()
                return location.json()
        except exc.IntegrityError:
            return "The code already exists!"

    @AuthService.tokenRequired
    def getLocationByCode(self, code):
        """Returns JSON object of a location"""
        location = Location.findLocationByCode(code)
        if location:
            return location.json(), 201
        return {"message": "The location is not found in the database."}, 404

    @AuthService.adminRequired
    def removeLocation(self, id):
        """Returns JSON object of deleted location"""
        location = Location.findLocationById(id)
        if location:
            location.delete()
            return {"message": "The location with id '{}' is deleted!".format(id)}
        else:
            return "The Location does not exist!"

    @AuthService.tokenRequired
    def getAllLocations(self):
        """Returns JSON object of all locations"""
        return list(map(lambda x: x.json(), Location.findAllLocations()))

    @AuthService.tokenRequired
    def getLocationByIds(self):
        """Returns JSON object of locations"""
        data = request.get_json(force=True)
        locations = []
        for x in data:
            location = Location.findLocationById(x)
            locations.append(location)
        return list(map(lambda x: x.json(), locations))