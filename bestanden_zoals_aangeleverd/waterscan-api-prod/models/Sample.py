from Database import db
from _datetime import datetime
import json

class Sample(db.Model):
    __tablename__ = "sample"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    quality = db.Column(db.Float)
    x_coor = db.Column(db.Integer)
    y_coor = db.Column(db.Integer)
    date_added = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    taxon_values = {}

    def __init__(self, id, date, quality, x_coor, y_coor, date_added, location_id, owner_id, taxon_values):
        self.id = id
        self.date = date
        self.quality = quality
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.date_added = date_added
        self.location_id = location_id
        self.owner_id = owner_id
        self.taxon_values = taxon_values

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "date": json.dumps(self.date, indent=4, sort_keys=True, default=str), "quality": self.quality, "x_coor": self.x_coor,
                "y_coor": self.y_coor, "date_added": json.dumps(self.date_added, indent=4, sort_keys=True, default=str), "location_id": self.location_id, "owner_id ": self.owner_id,
                "taxonValues": self.taxon_values}

    @classmethod
    def findSampleById(cls, id):
        """Returns the data of a specific sample chosen by id"""
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findAllSamples(cls):
        """Returns the data of all samples"""
        return cls.query.all()

    @classmethod
    def findAllSamplesByLocationId(cls, location_id):
        """Returns the data of all samples chosen by location id"""
        return cls.query.filter_by(location_id = location_id)


    def findRecentSamples(cls, count):
        """Returns the data of the recent samples limited by count"""
        return db.session.query(Sample).order_by(Sample.date_added.desc()).limit(count)

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()

