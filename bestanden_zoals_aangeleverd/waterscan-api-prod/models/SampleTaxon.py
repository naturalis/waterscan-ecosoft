from sqlalchemy import PrimaryKeyConstraint

from Database import db
from models.Taxon import Taxon
from models.WewValue import WewValue

# @author: Wim van der Putten
class SampleTaxon(db.Model):
    __tablename__ = "sample_taxon"

    # composite primarykey
    __table_args__ = (
        PrimaryKeyConstraint('sample_id', 'taxon_id'),
    )
    sample_id = db.Column(db.Integer, db.ForeignKey("sample.id"))
    taxon_id = db.Column(db.Integer, db.ForeignKey("taxon.id"))
    value = db.Column(db.Integer)

    def __init__(self, sample_id, taxon_id, value, taxon):
        self.sample_id = sample_id
        self.taxon_id = taxon_id
        self.value = value
        self.taxon = taxon

    # custom init for the sampleList
    def __init__(self, sample_id, taxon, wew_value):
        self.sample_id = sample_id
        self.taxon = taxon
        self.wew_value = wew_value

    def json(self):
        """Returns the models data converted to JSON"""
        return {"sample_id": self.sample_id, "taxon": self.taxon, "wew_value": self.wew_value}

    @classmethod
    def findTaxonListBySampleId(cls, id):
        """Returns the data of all taxa chosen by sample id"""
        query = db.session.query(cls, Taxon, WewValue)\
            .join(Taxon).filter(cls.sample_id == id)\
            .join(WewValue, WewValue.taxon_id == Taxon.id)\
            .all()
        return query


