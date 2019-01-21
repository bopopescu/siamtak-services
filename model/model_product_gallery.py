from sqlalchemy import select, func
from sqlalchemy import  Table, Column, DateTime, String, Text, text, desc, ForeignKey, asc
from sqlalchemy.dialects.mysql import ENUM, INTEGER
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship, backref, column_property, query
from sqlalchemy.ext.declarative import declarative_base

from db import db

class TblProductGallery(db.Model):
    __tablename__ = 'tbl_product_gallery'
    gallery_ID      = db.Column(db.Integer, primary_key=True)
    product_ID      = db.Column(db.String(120), nullable=False)
    gallery_PicThumb = db.Column(db.String(120), nullable=False)

    def json(self):
        return {c: str(getattr(self, c)) for c in inspect(self).attrs.keys()}

    # def findList(cls, key1):
    #     queryset = cls.query
    #
    #     queryset = queryset.filter(TblProductGallery.product_ID == key1).\
    #                all()
    #     return queryset

    @classmethod
    def findByValues(cls,  value):

        return cls.query.all()
