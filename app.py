from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from db import db
from resource.product import Product, ProductList, ProductHomeList
from resource.banner  import BannerList
import datetime
import pymysql

app = Flask(__name__)
api = Api(app)
app.secret_key = 'IDMAX'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://siamtak_usr:Saim@22333@27.254.59.108:3306/siamtak_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_SECRET_KEY'] = 'secret-test'

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('salt',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
 
api.add_resource(BannerList, '/banners')
api.add_resource(ProductList, '/product-lists')
api.add_resource(ProductHomeList, '/product-home-lists')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True
