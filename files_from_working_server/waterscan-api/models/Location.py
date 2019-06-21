from Database import db

class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))
    description = db.Column(db.String(100))
    x_coor = db.Column(db.Integer)
    y_coor = db.Column(db.Integer)
    waterschap_id = db.Column(db.Integer, db.ForeignKey("waterschap.id"))
    watertype_id = db.Column(db.Integer, db.ForeignKey("watertype.id"))
    watertype_krw_id = db.Column(db.Integer, db.ForeignKey("watertype.id"))

    # TODO IN IPSEN5, AANPASSEN
    latitude = 0
    longitude = 0

    def __init__(self, id, code, description, x_coor, y_coor, waterschap_id, watertype_id, watertype_krw_id):
        self.id = id
        self.code = code
        self.description = description
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.waterschap_id = waterschap_id
        self.watertype_id = watertype_id
        self.watertype_krw_id = watertype_krw_id

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "code": self.code, "description": self.description, "xCoor": self.x_coor, "yCoor": self.y_coor, "latitude": self.latitude,
                "longitude": self.longitude, "waterschapId": self.waterschap_id, "watertypeId": self.watertype_id, "watertypeKrwId": self.watertype_krw_id}

    @classmethod
    def findLocationById(cls, id):
        """Returns the data of a specific location chosen by id"""
        return cls.query.filter_by(id=id).first()

    @classmethod
    def findLocationByIds(cls, ids):
        """Returns the data of specific locations chosen by ids"""
        for id in ids:
            return cls.query.filter_by(id=id[id])

    @classmethod
    def findLocationByCode(cls, code):
        """Returns the data of a specific location chosen by code"""
        return cls.query.filter_by(code = code).first()

    @classmethod
    def findAllLocations(cls):
        """Returns the data of all locations"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()
