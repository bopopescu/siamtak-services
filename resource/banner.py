from flask import request, jsonify
from flask_restful import Resource, reqparse
#from flask_jwt_extended import jwt_required
from model.model_banner import TblBanners
import datetime
import json
from config import urlEndPoint

class BannerList(Resource):
    # @jwt_required
    def get(self):
        try:
            params = request.args
            dataLists = TblBanners.findList(params)
            results = []

            for dataList in dataLists:
                obj = {
                    'title'     : dataList.banner_Name,
                    'pic'       : urlEndPoint+'/banner/'+dataList.banner_pic,
                    'pic_mobile': urlEndPoint+'/banner/'+dataList.banner_pic2
                }
                results.append(obj)
            response = jsonify(results)
            return {'status': 'success', 'data': results}, 200

        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 500
