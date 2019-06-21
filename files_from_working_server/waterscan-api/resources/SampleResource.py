from flask_restful import Resource
from services.SampleService import SampleService

class SampleResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return SampleService.getSample(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return SampleService.updateSample(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return SampleService.addSample(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return SampleService.removeSample(self, id)

class SamplesResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return SampleService.getAllSamples(self)

class SampleByLocationResource(Resource):
    def get(self, locationId):
        """GET request for this resource layer passes it to service layer"""
        return SampleService.getAllSamplesByLocation(self, locationId)

class SampleYearsResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return SampleService.getSampleYears(self)

class RecentSamples(Resource):
    def get(self, count):
        """GET request for this resource layer passes it to service layer"""
        return SampleService.getRecentSample(self, count)