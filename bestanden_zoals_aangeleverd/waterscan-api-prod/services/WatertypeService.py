from models.Watertype import Watertype
from flask_restful import reqparse
from flask import request
from sqlalchemy import exc
from services.AuthService import AuthService

class WatertypeService:
    # Create a parser so the JSON can be checked
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="ID cannot be left blank!")
    parser.add_argument("name", type=str, required=True, help="Name cannot be left blank!")
    parser.add_argument("code", type=str, required=True, help="Code cannot be left blank!")

    # This method retrieves a watertype from the database by ID
    @AuthService.tokenRequired
    def getWaterType(self, id):
        watertype = Watertype.findWatertypeById(id)
        if watertype:
            return watertype.json(), 201
        return {"message": "The watertype is not found in the database."}, 404

    # This method retrieves all watertypes from the database
    @AuthService.tokenRequired
    def getAllWatertypes(self):
        return list(map(lambda x: x.json(), Watertype.findAllWatertypes()))

    # This method updates a watertype
    @AuthService.adminRequired
    def updateWaterType(self, id):
        try:
            data = WatertypeService.parser.parse_args()
            watertype = Watertype.findWatertypeById(data["id"])

            if watertype:
                watertype.name = data["name"]
                watertype.code = data["code"]
            else:
                watertype = Watertype(data["id"], data["name"], data["code"])

            watertype.save()
            return watertype.json()
        except exc.IntegrityError:
            return "Duplicate Name or Code!"

    # This method creates, and only creates a watertype
    @AuthService.adminRequired
    def addWaterType(self, id):
        try:
            data = WatertypeService.parser.parse_args()
            watertype = Watertype.findWatertypeById(data["id"])

            if watertype:
                return "The watertype already exists!"
            else:
                watertype = Watertype(data["id"], data["name"], data["code"])
                watertype.save()
                return watertype.json()
        except exc.IntegrityError:
            return "Duplicate name or code!"

    # This method removes a watertype from the database
    @AuthService.adminRequired
    def removeWatertype(self, id):
        watertype = Watertype.findWatertypeById(id)
        if watertype:
            watertype.delete()
            return {"message": "The watertype with id '{}' is deleted!".format(id)}
        else:
            return "The watertype does not exist!"