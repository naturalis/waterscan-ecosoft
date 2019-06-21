from flask_restful import Resource

from models.Location import Location
from services.WewService import WewService

class WewResource(Resource):
    def get(self):
        """GET request for this resource layer, returns all locations in JSON"""
        return {"locations": list(map(lambda x: x.json(), Location.query.all()))}

class WewFactorResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return WewService.getFactors(self)

    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return WewService.saveFactors(self)

class WewValueResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return WewService.saveValue(self)

class WewAdminResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return WewService.isEmpty(self)

class WewAdminEmptyResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return WewService.emptyTables(self)

class TaxonWewValueResource(Resource):
    def get(self, taxonId):
        """GET request for this resource layer passes it to service layer"""
        return WewService.getTaxonWewValue(self, taxonId)