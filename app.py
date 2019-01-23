from flask import Flask, jsonify
from flask_restful import Api

from flask_jwt import JWT, jwt_required, current_identity

from db import connection

# from model.amphur import amphurList

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/amphur')
def home():
     with connection.cursor() as cursor:
     cursor.execute("SELECT * FROM tbl_amphur")
     rv = cursor.fetchall()
     return jsonify(rv)

# api.add_resource(model.amphurList, '/amphurs')


if __name__ == '__main__':

    app.run(debug=True, port=5000)  # important to mention debug=True
