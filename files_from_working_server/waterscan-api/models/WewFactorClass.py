from sqlalchemy import func

from Database import db

class WewFactorClass(db.Model):
    __tablename__ = "wew_factor_class"
    id = db.Column(db.Integer, primary_key=True)
    factor_id = db.Column(db.Integer, db.ForeignKey("wew_factor.id"))
    code = db.Column(db.String(10))
    description = db.Column(db.String(100))
    order = db.Column(db.Integer)
    computed_value = 0

    def __init__(self, id, factor_id, code, description, order):
        self.id = id
        self.factor_id = factor_id
        self.code = code
        self.description = description
        self.order = order
        self.computed_value = 0

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "factorId": self.factor_id, "code": self.code, "description": self.description, "order": self.order}

    def jsonComputed(self):
        """Returns the models data converted to JSON"""
        return {"factorClassId": self.id, "computedValue": self.computed_value}

    @classmethod
    def findAllFactors(cls):
        return cls.query.all()

    @classmethod
    def getComputedRefValue(cls, referenceId, factorClass):
       engine = db.engine
       return engine.execute(func.calc_computed_value_ref(referenceId, factorClass)).fetchone()[0]

    @staticmethod
    def delete():
        """Empties the table specified in the model"""
        db.session.execute("SET FOREIGN_KEY_CHECKS = 0; TRUNCATE TABLE wew_factor_class; SET FOREIGN_KEY_CHECKS = 1;")
        db.session.commit()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()