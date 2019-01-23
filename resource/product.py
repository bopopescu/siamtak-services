from flask import request, jsonify
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from model.model_product import TblProduct
from model.model_product_gallery import TblProductGallery
import datetime
import json
from config import urlEndPoint

class Product(Resource):
    #@jwt_required
    def get(self, pk):
        try:
            data = TblProduct.read(pk)
            if not data:
                return {'status': 'fail', 'message': 'Product not found'}, 404
            return {'status': 'ok', 'data': data.json()}, 200
        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 500

class ProductList(Resource):
    # @jwt_required
    def get(self):
        try:
            params = request.args

            dataLists = TblProduct.findHomeList(params)
            results = []

            for dataList in dataLists:
                obj = {

                    'title'     : dataList.product_Name,
                    'title_en'  : dataList.product_NameEN,
                    'detail'    : dataList.product_detail,
                    'detail_en' : dataList.product_detailen,
                    'price'     : dataList.product_Price,
                    'pic'       : urlEndPoint+'/products/'+dataList.product_pic,
                    'pic_thumb' : urlEndPoint+'/products/'+dataList.product_picThumb,
                }
                results.append(obj)
            response = jsonify(results)

            return {'status': 'success', 'data': results}, 200

        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 500

class ProductHomeList(Resource):
    # @jwt_required
    def get(self):
        try:
            params = request.args
            #data = [item.json() for item in TblProduct.findHomeList(params)]
            #results = [item.json() for item in TblProductGallery.findByValues('11')]

            dataLists = TblProduct.findHomeList(params)
            dataGalleryLists = TblProductGallery.findByValues(params)
            results = []

            for dataList in dataLists:

                resultsGalley = []
                for dataGalleryList in dataGalleryLists:
                    if dataList.product_id == dataGalleryList.product_ID:
                        objGallery = {
                            'pic'     : urlEndPoint+'/products/'+dataGalleryList.gallery_PicThumb,
                        }
                        resultsGalley.append(objGallery)

                obj = {

                    'title'     : dataList.product_Name,
                    'title_en'  : dataList.product_NameEN,
                    'detail'    : dataList.product_detail,
                    'detail_en' : dataList.product_detailen,
                    'price'     : dataList.product_Price,
                    'pic'       : urlEndPoint+'/products/'+dataList.product_pic,
                    'pic_thumb' : urlEndPoint+'/products/'+dataList.product_picThumb,
                    'gallery'   : resultsGalley
                }
                results.append(obj)
            response = jsonify(results)

            return {'status': 'success', 'data': results}, 200

        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 500
