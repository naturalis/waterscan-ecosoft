from sqlalchemy import text, or_
from sqlalchemy.orm import aliased

from Database import db
from models.Location import Location
from models.Sample import Sample
from models.Watertype import Watertype

# @author: Wim van der Putten
class Marker(Sample):
    def __init__(self, location, watertype, watertypeKrw, lastTakenSample):
        self.location = location
        self.watertype = watertype
        self.watertypeKrw = watertypeKrw
        self.lastTakenSample = lastTakenSample

    def json(self):
        """Returns the models data converted to JSON"""
        return {"location": self.location, "watertype": self.watertype, "watertypeKrw": self.watertypeKrw, "lastTakenSample": self.lastTakenSample}

    @classmethod
    def marker(cls, waterschapId = 0, watertype= 0, date= ""):
        """Returns the markers needed for the map"""
        #creating filters
        if int(waterschapId) != 0:
            waterschapFilter = (Location.waterschapId == waterschapId)
            print(waterschapId)
        else:
            waterschapFilter= text('1=1')

        if int(watertype)!= 0:
            watertypeFilter = (or_(Location.watertypeId == watertype, Location.watertypeKrwId == watertype))
            print(watertype)
        else:
            watertypeFilter= text('1=1')

        if date != "":
            dateFilter = (Sample.date >= date)
        else:
            dateFilter= text('1=1')
        watertypeKrw = aliased(Watertype, name="watertypeKrw")

        query = db.session.query(Sample, Location, Watertype, watertypeKrw) \
            .join(Location) \
            .join(Watertype, Location.watertype_id==Watertype.id) \
            .join(watertypeKrw, Location.watertype_krw_id==watertypeKrw.id) \
            .filter(waterschapFilter) \
            .filter(watertypeFilter)
        return query
