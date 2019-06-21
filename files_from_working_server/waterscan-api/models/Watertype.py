from Database import db

class Watertype(db.Model):
    __tablename__ = "watertype"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(10))

    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "name": self.name, "code": self.code}

    @classmethod
    def findWatertypeById(cls, id):
        """Returns the data of a watertype chosen by id"""
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findAllWatertypes(cls):
        """Returns the data of all watertypes"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()