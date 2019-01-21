# coding: utf-8
from flask import request, jsonify
from sqlalchemy import select, func
from sqlalchemy import  Table, Column, DateTime, String, Text, text, desc, ForeignKey, asc
from sqlalchemy.dialects.mysql import ENUM, INTEGER
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship, backref, column_property, query
from sqlalchemy.ext.declarative import declarative_base

from db import db

class TblBanners(db.Model):

    __tablename__ = 'tbl_banner'
    banner_ID = db.Column(db.Integer, primary_key=True)
    banner_Name = db.Column(db.String(120), nullable=False)
    banner_pic = db.Column(db.String(120), nullable=False)
    banner_pic2 = db.Column(db.String(120), nullable=False)
    banner_publish = db.Column(db.String(120), nullable=False)
    banner_OrderBy = db.Column(db.String(120), nullable=False)

    def json(self):
        return {c: str(getattr(self, c)) for c in inspect(self).attrs.keys()}

    @classmethod
    def findList(cls, cond):
        queryset = cls.query
        queryset = queryset.filter(TblBanners.banner_publish == '1').\
                   order_by(asc(TblBanners.banner_OrderBy)).\
                   limit(10).all()

        return queryset
