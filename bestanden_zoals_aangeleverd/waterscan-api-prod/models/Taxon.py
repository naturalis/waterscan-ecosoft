from Database import db

class Taxon(db.Model):
    __tablename__ = "taxon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    group_id = db.Column(db.Integer, db.ForeignKey("taxon_group.id"))
    level_id = db.Column(db.Integer, db.ForeignKey("taxon_level.id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("taxon.id"))
    refer_id = db.Column(db.Integer, db.ForeignKey("taxon.id"))
    hydrologische_verstoring = db.Column(db.Integer)
    morfologische_verstoring = db.Column(db.Integer)
    eutrofiering_belasting = db.Column(db.Integer)

    def __init__(self, id, name, group_id, level_id, parent_id, refer_id, hydrologische_verstoring,
                 morfologische_verstoring, eutrofiering_belasting):
        self.id = id
        self.name = name
        self.group_id = group_id
        self.level_id = level_id
        self.parent_id = parent_id
        self.refer_id = refer_id
        self.hydrologische_verstoring = hydrologische_verstoring
        self.morfologische_verstoring = morfologische_verstoring
        self.eutrofiering_belasting = eutrofiering_belasting

    def json(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "name": self.name, "groupId": self.group_id, "levelId": self.level_id,
                "parentId": self.parent_id}

    def jsonSample(self):
        """Returns the models data converted to JSON"""
        return {"id": self.id, "name": self.name, "hydrologischeVerstoring": self.hydrologische_verstoring, "morfologischeVerstoring": self.morfologische_verstoring, "eutrofieringBelasting": self.eutrofiering_belasting}

    @classmethod
    def findTaxonById(cls, id):
        """Returns the data of a specific taxon chosen by id"""
        return cls.query.filter_by(id=id).first()

    @classmethod
    def findAllTaxons(cls):
        """Returns the data of all taxons"""
        return cls.query.all()

    @classmethod
    def findTaxonByIds(cls, ids):
        """Returns the data of specific taxa chosen by ids"""
        for id in ids:
            return cls.query.filter_by(id=id[id])
        pass

    @classmethod
    def findTaxonByName(cls, name):
        """Returns the data of specific taxa chosen by name"""
        return cls.query.filter_by(name=name).first()

    @classmethod
    def findParentById(cls, parentId):
        """Returns the data of a specific parent taxon chosen by id"""
        return cls.query.filter_by(id = parentId).first()

    @classmethod
    def findChildrenById(cls, id):
        """Returns the data of a specific child taxon chosen by id"""
        return cls.query.filter_by(parent_id=id).all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()
