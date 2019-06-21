from Database import db

class TaxonGroup(db.Model):
    __tablename__ = "taxon_group"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8))
    description = db.Column(db.String(100))
    icon = db.Column(db.String(50))

    def __init__(self, id, code, description, icon):
        self.id = id
        self.code = code
        self.description = description
        self.icon = icon

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "code": self.code, "description": self.description, "icon": self.icon}

    @classmethod
    def findTaxonGroupById(cls, id):
        """Returns the data of a specific taxon group chosen by id"""
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findAllTaxonGroups(cls):
        """Returns the data of all taxon groups"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()