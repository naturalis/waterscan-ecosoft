from Database import db
import datetime

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    name = db.Column(db.String(100))
    session_token = db.Column(db.String(36))
    expiration_date = db.Column(db.DateTime, default=datetime.datetime.now)
    group_id = db.Column(db.Integer, db.ForeignKey("user_group.id"))
    waterschap_id = db.Column(db.Integer, db.ForeignKey("waterschap.id"))

    def __init__(self, id, email, password, name, session_token, expiration_date, group_id, waterschap_id):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.group_id = group_id
        self.waterschap_id = waterschap_id

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "email": self.email, "password": self.password, "name": self.name,
                "groupId": self.group_id, "waterschapId": self.waterschap_id}

    @classmethod
    def findUserById(cls, id):
        """Returns the data of a user chosen by id"""
        return cls.query.filter_by(id=id).first()

    @classmethod
    def findUserByEmail(cls, email):
        """Returns the data of a user chosen by email"""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def findAllUsers(cls):
        """Returns the data of all users"""
        return cls.query.all()

    def updateUser(self):
        """Saves the user data to an existing user"""
        db.session.commit()

    def addUser(self):
        """Saves the user data to an new user"""
        db.session.add(self)
        db.session.commit()

    def removeUser(self):
        """Deletes the user from the table"""
        db.session.delete(self)
        db.session.commit()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()