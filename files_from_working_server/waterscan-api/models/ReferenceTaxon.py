from sqlalchemy import PrimaryKeyConstraint

from Database import db
from models.Taxon import Taxon
from models.WewValue import WewValue

class ReferenceTaxon(db.Model):
    __table_args__ = (
        PrimaryKeyConstraint('reference_id', 'taxon_id'),
    )
    reference_id = db.Column(db.Integer, db.ForeignKey("reference.id"))
    taxon_id = db.Column(db.Integer, db.ForeignKey("taxon.id"))

    def __init__(self, reference_id, taxon_id):
        self.reference_id = reference_id
        self.taxon_id = taxon_id

    # custom init for the sampleList
    def __init__(self, reference_id, taxon, wew_value):
        self.reference_id = reference_id
        self.taxon = taxon
        self.wew_value = wew_value

    def json(self):
        """Returns the models data converted to JSON"""
        return {"ReferenceId": self.reference_id, "TaxonId": self.taxon_id}

    def jsonValue(self):
        """Returns the models data converted to JSON"""
        return {"reference_id": self.reference_id, "taxon": self.taxon, "wew_value": self.wew_value}

    @classmethod
    def findTaxonListBySampleId(cls, id):
        """Returns the data of all taxa chosen by sample id"""
        query = db.session.query(cls, Taxon, WewValue) \
            .join(Taxon).filter(cls.reference_id == id) \
            .join(WewValue, WewValue.taxon_id == Taxon.id) \
            .all()
        return query

    @classmethod
    def findReferenceById(cls, reference_id):
        """Returns the data of a specific reference chosen by id"""
        return cls.query.all()

    def save(self):
        """Saves the object to the table specified in the model"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the object from the table specified in the model"""
        db.session.delete(self)
        db.session.commit()