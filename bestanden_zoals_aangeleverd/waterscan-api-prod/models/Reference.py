from Database import db

class Reference(db.Model):
    __tablename__ = "reference"
    id = db.Column(db.Integer, primary_key=True)
    watertype_id = db.Column(db.Integer)

    def __init__(self, id, watertype_id):
        self.id = id
        self.watertype_id = watertype_id

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "watertypeId": self.watertype_id}

    @classmethod
    def getReference(cls, id):
        """Returns the data of a specific reference chosen by id"""
        return cls.query.filter_by(id = id).first()

    @classmethod
    def getAllReferences(cls):
        """Returns the data of all references"""
        return cls.query.all()

    @classmethod
    def findReferencesByWatertype(cls, watertype_id):
        """Returns the data of a specific reference chosen by watertype id"""
        return cls.query.filter_by(watertype_id = watertype_id).first()