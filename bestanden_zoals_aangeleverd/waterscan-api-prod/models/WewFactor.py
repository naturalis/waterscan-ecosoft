from Database import db

class WewFactor(db.Model):
    __tablename__ = "wew_factor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1 - 0))
    classes = {}

    def __init__(self, id, name):
        self.classes = []
        self.id = id
        self.name = name

    def json(self):
        """Returns the models data converted to JSON"""
        return {"classes": self.classes, "id": self.id, "name": self.name}

    @staticmethod
    def delete():
        """Empties the table specified in the model"""
        db.session.execute("SET FOREIGN_KEY_CHECKS = 0; TRUNCATE TABLE wew_factor; SET FOREIGN_KEY_CHECKS = 1;")
        db.session.commit()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()