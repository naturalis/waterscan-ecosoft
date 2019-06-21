from Database import db

class reference_wew_factor_class_temp(db.Model):
    __tablename__ = "reference_wew_factor_class"
    id = db.Column(db.Integer, primary_key=True)
    reference_id = db.Column(db.Integer, db.ForeignKey("reference.id"))
    factor_class_id = db.Column(db.Integer, db.ForeignKey("wew_factor_class.id"))
    computed_value = db.Column(db.Integer)

    def __init__(self, id, reference_id, factor_class_id, computed_value):
        self.id = id
        self.reference_id = reference_id
        self.factor_class_id = factor_class_id
        self.computed_value = computed_value

    def jsonComputed(self):
        """Returns the models data converted to JSON"""
        return {"factorClassId": self.id, "computedValue": self.computed_value}

    @classmethod
    def findAllFactors(cls, refId):
        """Returns the data of all factors"""
        return cls.query.filter(cls.reference_id == refId)
