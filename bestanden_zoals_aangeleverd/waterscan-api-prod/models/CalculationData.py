from Database import db

class CalculationData(db.Model):
    __tablename__ = "sample_wew_factor_class"
    id = db.Column(db.Integer, primary_key=True)
    sample_id = db.Column(db.Integer)
    factor_class_id = db.Column(db.Integer)
    computed_value = db.Column(db.Float)

    def __init__(self, factor_class_id, computed_value):
        self.factor_class_id = factor_class_id
        self.computed_value = computed_value

    def json(self):
        """Returns the models data converted to JSON"""
        return {"factorClassId": self.factor_class_id, "computedValue": self.computed_value}

    @classmethod
    def findCalculationBySampleId(cls, id):
        """Returns the wew value of each ecological variable of a specific sample chosen by id"""
        return cls.query.filter_by(sample_id=id)
