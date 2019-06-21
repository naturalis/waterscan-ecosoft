from flask import request
from services.AuthService import AuthService
from models.Marker import Marker
from services.ConverterService import ConverterService

# @author: Wim van der Putten
class MapService:
    @AuthService.tokenRequired
    def getMarkersByFilter(self):
        waterschapId = 0
        watertypeId = 0
        date = ''

        if 'waterschapId' in request.get_json():
            waterschapId = request.get_json()['waterschapId']

        if 'watertypeId' in request.get_json():
            watertypeId = request.get_json()['watertypeId']

        if 'date' in request.get_json():
            date = request.get_json()['date']

        results = Marker.marker(waterschapId, watertypeId, date);
        markers = []
        for result in results:
            location = result.Location
            coords = ConverterService.convert(self, location)
            location.latitude = coords.latitude
            location.longitude = coords.longitude
            markers.append(Marker(location.json(), result.Watertype.json(), result.watertypeKrw.json(), "00-00-0000"));
        return list(map(lambda x: x.json(), markers))
