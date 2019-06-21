from models.Reference import Reference
from flask import request

from services.AuthService import AuthService
class ReferenceService:
    def getReference(self):
        id = request.headers.get("id")

    @AuthService.tokenRequired
    def getReference(self, id):
        reference = Reference.getReference(id)
        if reference:
            return reference.json(), 201
        return {"message": "The location is not found in the database."}, 404

    @AuthService.tokenRequired
    def getAllReferences(self):
        return list(map(lambda x: x.json(), Reference.getAllReferences()))

    @AuthService.tokenRequired
    def getReferenceWatertype(self, watertype_id):
        waterReference = Reference.findReferencesByWatertype(watertype_id)
        if waterReference:
            return waterReference.json(), 201
        return {"message": "The location is not found in the database."}, 404
