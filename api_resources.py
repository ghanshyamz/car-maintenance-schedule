
from datetime import datetime
from unittest import result
from warnings import catch_warnings
from flask_restful import Resource, reqparse
from pony.orm import db_session, commit, core, select
from models import User, Car, Servicing
from pony.orm.serialization import to_dict

user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, help="Name of the user",  required=True)
user_args.add_argument("phone_no", type=str, help="Phone number of the user",  required=True)

car_args = reqparse.RequestParser()
car_args.add_argument("model", type=str, help="company and model, eg. Maruti 800")
car_args.add_argument("color", type=str, help="")
car_args.add_argument("ownerid", type=int, help="Owner's Id")
car_args.add_argument("purchase_date", type=str, help="Purchase Date in YYYY/MM/DD format")

servicing_args = reqparse.RequestParser()
servicing_args.add_argument("carid", type=int, help="Car Id")
servicing_args.add_argument("servicing_date", type=str, help="Servicing Date in YYYY/MM/DD format", required=True)
servicing_args.add_argument("status", type=str, help="Servicing status")

# user resources
class UserCreate(Resource):
    def post(self):
        # content_type = request.headers.get('Content-Type')
        # if (content_type == 'application/json'):
        args = user_args.parse_args(strict=True)
        with db_session:
            try:
                User(name= args.name, phone_no=args.phone_no)
                commit()
            except core.TransactionIntegrityError as e:
                return { "error" : 1, 'error-message': "Phone number already exist!" }
            except Exception as e:
                return { "error" : 1, 'error-message': e.args }
        
        return { "error" : 0, 'error-message': "" }


class UserGetAll(Resource):
    @db_session
    def get(self):
        users = select(u for u in User)[:]
        result = [u.to_dict() for u in users]
        print(users)
        return { "error" : 0, 'error-message': "" , "Users": result}

class UserGet(Resource):
    @db_session
    def get(self, id):
        try:
            user = User[id]
            result = to_dict(user)
            user_data = result['User'][id]
            car_ids = result['User'][id]['cars']

            user_data['Cars'] = [result['Car'][id] for id in car_ids]
            del user_data['cars']
            # converting datetime to string
            for i in user_data['Cars']:
                if type(i['purchase_date']) is datetime:
                    i['purchase_date'] = i['purchase_date'].strftime(r"%Y/%m/%d")

            print(user_data)

        except core.ObjectNotFound as e:
            return { "error" : 1, 'error-message': "Object not found!" , "User": ""}, 404

        return { "error" : 0, 'error-message': "" , "User": user_data}


# car resources
class CarCreate(Resource):
    def post(self):
        args = car_args.parse_args(strict=True)
        with db_session:
            try:
                Car(model= args.model, color=args.color, owner=args.ownerid, purchase_date=args.purchase_date)
                commit()
            except Exception as e:
                return { "error" : 1, 'error-message': e.args }, 404
        
        return { "error" : 0, 'error-message': "" }

class CarGetAll(Resource):
    @db_session
    def get(self):
        cars = select(c for c in Car)[:]
        result = [c.to_dict() for c in cars]

        # converting datetime to string
        for i in result:
            if type(i['purchase_date']) is datetime:
                i['purchase_date'] = i['purchase_date'].strftime(r"%Y/%m/%d")
            if i['owner']:
                del i['owner']

        return { "error" : 0, 'error-message': "" , "Cars": result}

class CarGet(Resource):
    @db_session
    def get(self, id):
        try:
            car = Car[id]
            result = to_dict(car)
            print(result)
            car_data = result['Car'][id]
            del car_data['owner']
            car_data['purchase_date'] = car_data['purchase_date'].strftime(r"%Y/%m/%d")
            servicing_ids = result['Car'][id]['services']

            car_data['Servicing'] = [result['Servicing'][id] for id in servicing_ids]
            print(car_data)
            del car_data['color']
            del car_data['services']
            for servicing in car_data['Servicing']:
                del servicing['car']
                servicing['servicing_date'] = servicing['servicing_date'].strftime(r"%Y/%m/%d")

            print(car_data)

        except core.ObjectNotFound as e:
            return { "error" : 1, 'error-message': "Object not found!" , "Cars": ""}, 404

        return { "error" : 0, 'error-message': "" , "Car": car_data}

# serviving resources
class ServicingCreate(Resource):
    @db_session
    def post(self):
        args = servicing_args.parse_args(strict=False)
        with db_session:
            try:
                Servicing(car= args.carid, servicing_date=args.servicing_date, status=args.status)
                commit()
            except Exception as e:
                return { "error" : 1, 'error-message': e.args }
        
        return { "error" : 0, 'error-message': "" }

class ServicingGetAll(Resource):
    @db_session
    def get(self):
        servicings = select(s for s in Servicing)[:]
        result = [s.to_dict() for s in servicings]

        # converting datetime to string
        for i in result:
            if type(i['servicing_date']) is datetime:
                i['servicing_date'] = i['servicing_date'].strftime(r"%Y/%m/%d")
            if i['car']:
                del i['car']


        return { "error" : 0, 'error-message': "" , "Servicings": result}
