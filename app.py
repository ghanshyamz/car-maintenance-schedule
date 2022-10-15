from flask import Flask, render_template, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from pony.orm import Database, set_sql_debug

app = Flask(__name__)

from models import *
import api_resources


# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
# db = SQLAlchemy(app)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')




db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(True)



api = Api(app)


# User endpoints
api.add_resource(api_resources.UserCreate, '/user/create')
api.add_resource(api_resources.UserGetAll, '/user/getall')
api.add_resource(api_resources.UserGet, '/user/get/<int:id>')

# Car endpoints
api.add_resource(api_resources.CarCreate, '/car/create')
api.add_resource(api_resources.CarGetAll, '/car/getall')
api.add_resource(api_resources.CarGet, '/car/get/<int:id>')

# Servicing endpoints
api.add_resource(api_resources.ServicingCreate, '/servicing/create')
api.add_resource(api_resources.ServicingGetAll, '/servicing/getall')

if __name__ == "__main__":
    app.run(debug=True)