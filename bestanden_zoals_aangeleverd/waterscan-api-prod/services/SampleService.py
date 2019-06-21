from models.Sample import Sample
from flask_restful import reqparse
from services.AuthService import AuthService

class SampleService:
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="ID cannot be left blank!")
    parser.add_argument("date")
    parser.add_argument("quality", type=float, required=True, help="Quality cannot be left blank!")
    parser.add_argument("x_coor", type=int, required=True)
    parser.add_argument("y_coor", type=int, required=True, help="Y Coordinate cannot be left blank!")
    parser.add_argument("date_added")
    parser.add_argument("location_id", type=int, required=True, help="Location ID cannot be null")
    parser.add_argument("owner_id", type=int)
    parser.add_argument("taxon_values")

    # Get a sample by the id in the header
    @AuthService.tokenRequired
    def getSample(self, id):
        sample = Sample.findSampleById(id)
        if sample:
            return sample.json(), 201
        return {"message": "The sample is not found!"}, 404

    # Updates a sample
    @AuthService.adminRequired
    def updateSample(self, id):
        data = SampleService.parser.parse_args()
        sample = Sample.findSampleById(id)

        if sample:
            sample.date = data["date"]
            sample.quality = data["quality"]
            sample.x_coor = data["x_coor"]
            sample.y_coor = data["y_coor"]
            sample.date_added = data["date_added"]
            sample.location_id = data["location_id"]
            sample.owner_id = data["owner_id"]
            sample.taxon_values = data["taxon_values"]
        else:
            sample = Sample(data["id"], data["date"], data["quality"], data["x_coor"], data["y_coor"],
                            data["date_added"], data["location_id"], data["owner_id"], data["taxon_values"])

        sample.save()
        return sample.json()

    # Creates, and only creates a sample.
    @AuthService.tokenRequired
    def addSample(self, id):
        data = SampleService.parser.parse_args()
        sample = Sample.findSampleById(id)

        if sample:
            return "Sample already exists!"
        else:
            sample = Sample(data["id"], data["date"], data["quality"], data["x_coor"], data["y_coor"],
                            data["date_added"], data["location_id"], data["owner_id"], data["taxon_values"])
            sample.save()
            return sample.json()

    # Deletes a sample from the database
    @AuthService.adminRequired
    def removeSample(self, id):
        sample = Sample.findSampleById(id)
        if sample:
            sample.delete()
            return {"message": "The sample with id '{}' is deleted!".format(id)}
        else:
            return "The sample does not exist!"

    @AuthService.tokenRequired
    def getAllSamples(self):
        return list(map(lambda x: x.json(), Sample.findAllSamples()))

    @AuthService.tokenRequired
    def getAllSamplesByLocation(self, locationId):
        return list(map(lambda x: x.json(), Sample.findAllSamplesByLocationId(locationId)))

    @AuthService.tokenRequired
    def getSampleYears(self):
        dates = list(map(lambda x: (x.date), Sample.findAllSamples()))
        years = []
        for date in dates:
            if date.year not in years:
                years.append(date.year)
        years.sort(reverse=True)
        return years

    def getRecentSample(self, count):
        return list(map(lambda x: x.json(), Sample.findRecentSamples(self, count)))
