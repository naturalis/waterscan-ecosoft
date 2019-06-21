from Database import db

class TaxonLevel(db.Model):
    __tablename__ = "taxon_level"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "name": self.name}

    @classmethod
    def findTaxonLevelById(cls, id):
        """Returns the data of a specific taxon level chosen by id"""
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findAllTaxonLevels(cls):
        """Returns the data of all taxon levels"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()