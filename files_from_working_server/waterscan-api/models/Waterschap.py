from Database import db

class Waterschap(db.Model):
    __tablename__ = "waterschap"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    house_number = db.Column(db.String(4))
    zip_code = db.Column(db.String(6))
    location = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))

    def __init__(self, id, name, address, house_number, zip_code, location, phone_number):
        self.id = id
        self.name = name
        self.address = address
        self.house_number = house_number
        self.zip_code = zip_code
        self.location = location
        self.phone_number = phone_number

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "name": self.name, "address": self.address, "house_number": self.house_number, "zip_code": self.zip_code, "location": self.location, "phone_number": self.phone_number}

    @classmethod
    def findWaterschapById(cls, id):
        """Returns the data of a waterschap chosen by id"""
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findWaterschapByName(cls, name):
        """Returns the data of a waterschap chosen by name"""
        return cls.query.filter_by(name = name).first()

    @classmethod
    def findAllWaterschappen(cls):
        """Returns the data of all waterschappen"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()
