# coding: utf-8
from sqlalchemy import select, func
from sqlalchemy import  Table, Column, DateTime, String, Text, text, desc, ForeignKey, asc
from sqlalchemy.dialects.mysql import ENUM, INTEGER
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship, backref, column_property, query
from sqlalchemy.ext.declarative import declarative_base

from db import db

class Tblcate(db.Model):
    __tablename__ = 'tbl_product_catagory'
    category_ID = db.Column(db.Integer, primary_key=True)
    category_Name = db.Column(db.String(120), nullable=False)
    categorys = db.relationship('TblProduct', back_populates="product_catagory")

class TblProduct(db.Model):
    __tablename__ = 'tbl_product'

    product_id = Column(INTEGER(10), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('tbl_product_catagory.category_ID'))
    product_catagory = relationship("Tblcate", back_populates="categorys")

    sub_categoryID = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    brand_ID = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    category_PromotionID = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    product_code = Column(String(30, 'utf8_unicode_ci'))
    product_pic = Column(String(30, 'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    product_picThumb =  Column(String(100, 'utf8_unicode_ci'), nullable=False, server_default=text("''"))
    product_StatusThumb = Column(ENUM('1', '2'), nullable=False, server_default=text("'1'"))
    product_Name = Column(String(255, 'utf8_unicode_ci'))
    product_NameEN = Column(String(255, 'utf8_unicode_ci'))
    # product_Abstract = Column(Text(collation='utf8_unicode_ci'))
    product_Price = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    product_Discount = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    product_priceSalesDateStart = Column(DateTime, nullable=False, server_default=text("'0000-00-00'"))
    product_priceSalesDateEnd = Column(DateTime, nullable=False, server_default=text("'0000-00-00'"))
    product_detail = Column(Text(collation='utf8_unicode_ci'))
    product_detailen = Column(Text(collation='utf8_unicode_ci'))
    product_superDeals = Column(ENUM('0', '1'), nullable=False, server_default=text("'0'"))
    #product_TotalSales = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    product_stockamount = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    product_statusbestseller = Column(ENUM('0', '1'), nullable=False, server_default=text("'0'"))

    product_SeoTitle = Column(String(255, 'utf8_unicode_ci'))
    product_SeoDescription = Column(Text(collation='utf8_unicode_ci'))
    product_SeoKeyword = Column(Text(collation='utf8_unicode_ci'))
    product_OrderBy = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    product_PromotionOrderBy = Column(INTEGER(5), nullable=False, server_default=text("'0'"))
    product_HotdealOrderBy = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    product_StockUpdateTime = Column(DateTime, nullable=False, server_default=text("'0000-00-00'"))
    product_Transport = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    product_CreateDate = Column(DateTime, nullable=False, server_default=text("'0000-00-00'"))
    product_update = Column(DateTime, nullable=False, server_default=text("'0000-00-00'"))
    product_publish = Column(ENUM('0', '1', '2'), server_default=text("'1'"))
    product_view = Column(INTEGER(10), nullable=False, server_default=text("'0'"))

    def json(self):
        return {c: str(getattr(self, c)) for c in inspect(self).attrs.keys()}

    @classmethod
    def findByValues(cls, field, value):
        return cls.query.filter_by(**{field : value}).first()

    @classmethod
    def findList(cls, cond):
        queryset = cls.query
        if 'product_code' in cond.keys() and cond['product_code'] != '':
            queryset = queryset.filter(TblProduct.product_code.like('%'+cond['product_code']+'%'))
        if 'product_View' in cond.keys() and cond['product_View'] != '':
            queryset = queryset.filter(TblProduct.product_View == cond['product_View'])
        #print(queryset)
        return queryset.order_by(asc(TblProduct.product_OrderBy)).all()

    @classmethod
    def findHomeList(cls, cond):
        queryset = cls.query
        if 'product_code' in cond.keys() and cond['product_code'] != '':
            queryset = queryset.filter(TblProduct.product_code.like('%'+cond['product_code']+'%'))
        if 'product_View' in cond.keys() and cond['product_View'] != '':
            queryset = queryset.filter(TblProduct.product_View == cond['product_View'])
        #print(queryset)
        #queryset = queryset.query.join(TblProduct, TblProduct.category_id==Tblcate.category_ID).all()
        queryset = queryset.filter(TblProduct.product_publish == '1').\
                   order_by(asc(TblProduct.product_OrderBy)).\
                   limit(100).all()
        return queryset


    @classmethod
    def read(cls, pk):
        return cls.query.get(pk)
