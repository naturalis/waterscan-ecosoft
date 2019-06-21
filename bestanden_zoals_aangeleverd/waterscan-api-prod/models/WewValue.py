from Database import db

class WewValue(db.Model):
    __tablename__ = "wew_value"
    id = db.Column(db.Integer, primary_key=True)
    factor_class_id = db.Column(db.Integer)
    taxon_id = db.Column(db.Integer)
    value = db.Column(db.Integer)

    def __init__(self, id, factor_class_id, taxon_id, value):
        self.id = id
        self.factor_class_id = factor_class_id
        self.taxon_id = taxon_id
        self.value = value

    def json(self):
        """Returns the models data converted to JSON"""
        return {"factor_class_id": self.factor_class_id, "value": self.value}
    
    @staticmethod
    def delete():
        """Empties the table specified in the model"""
        db.session.execute("SET FOREIGN_KEY_CHECKS = 0; TRUNCATE TABLE wew_value; SET FOREIGN_KEY_CHECKS = 1;")
        db.session.commit()
        
    def jsonTaxonWewValue(self):
        """Returns the models data converted to JSON"""
        return {"i": self.id, "c": self.factor_class_id, "t": self.taxon_id, "v": self.value}

    @classmethod
    def findWewValuesByTaxonId(cls, taxonId):
        """Returns the data of all wew values chosen by taxon id"""
        return cls.query.filter_by(taxon_id = taxonId).all()

    def jsonCalc(self):
        """Returns the models data converted to JSON"""
        return {"factor_class_id": self.factor_class_id, "value": self.value, "taxon_id": self.taxon_id}

    @classmethod
    def findAllWewValues(cls):
        """Returns the data of all wew values"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def bulkInsert(list):
        db.session.add_all(list)
        db.session.commit()

