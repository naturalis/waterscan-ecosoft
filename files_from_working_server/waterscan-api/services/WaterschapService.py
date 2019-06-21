from models.Waterschap import Waterschap
from flask_restful import reqparse
from flask import request
from sqlalchemy import exc
from services.AuthService import AuthService

class WaterschapService:
    # Create a parser so the JSON can be checked
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Name cannot be left blank!")
    parser.add_argument("address", type=str, required=True, help="Address cannot be left blank!")
    parser.add_argument("house_number", type=str, required=True, help="House number cannot be left blank!")
    parser.add_argument("zip_code", type=str, required=True, help="Zipcode cannot be left blank!")
    parser.add_argument("location", type=str, required=True, help="Location cannot be left blank!")
    parser.add_argument("phone_number", type=str, required=True, help="Phone number cannot be left blank!")

    # This method retrieves a waterschap from the database
    @AuthService.tokenRequired
    def getWaterschap(self, id):
        waterschap = Waterschap.findWaterschapById(id)
        if waterschap:
            return waterschap.json(), 201
        return {"message": "The waterschap is not found in the database."}, 404

    # This method updates a waterschap
    @AuthService.tokenRequired
    def getAllWaterschappen(self):
        return list(map(lambda x: x.json(), Waterschap.findAllWaterschappen()))

    @AuthService.adminRequired
    def updateWaterschap(self):
        try:
            data = WaterschapService.parser.parse_args()
            waterschap = Waterschap.findWaterschapById(id)

            if waterschap:
                waterschap.name = data["name"]
                waterschap.address = data["address"]
                waterschap.house_number = data["house_number"]
                waterschap.zip_code = data["zip_code"]
                waterschap.location = data["location"]
                waterschap.phone_number = data["phone_number"]
            else:
                waterschap = Waterschap(data["name"], data["address"], data["house_number"], data["zip_code"], data["location"], data["phone_number"])

            waterschap.save()
            return waterschap.json()
        except exc.IntegrityError:
            return "The name already exists!"

    # This method adds, and only adds a waterschap
    @AuthService.adminRequired
    def addWaterschap(self):
        try:
            data = request.json
            print(data)
            waterschap = Waterschap.findWaterschapByName(data["name"])
            if waterschap:
                return "The waterschap already exists!"
            else:
                waterschap = Waterschap(None, data["name"], data["address"], data["houseNumber"], data["zipCode"], data["location"], data["phoneNumber"])
                waterschap.save()
                return waterschap.json()
        except exc.IntegrityError:
            return "The name already exists!"

    # This method removes a waterschap
    @AuthService.adminRequired
    def removeWaterschap(self, id):
        waterschap = Waterschap.findWaterschapById(id)
        if waterschap:
            waterschap.delete()
            return {"message": "The waterschap with id '{}' is deleted!".format(id)}
        else:
            return "The waterschap does not exist!"

    def getAllWaterschappen(self):
        return list(map(lambda x: x.json(), Waterschap.findAllWaterschappen()))
