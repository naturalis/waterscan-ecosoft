from Database import db

class UserGroup(db.Model):
    __tablename__ = "user_group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "name": self.name}

    @classmethod
    def findUserGroupById(cls, id):
        """Returns the data of a user group chosen by id"""
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findAllUserGroups(cls):
        """Returns the data of all user groups"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()