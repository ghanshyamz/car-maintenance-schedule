from pony.orm import Required, Set
from datetime import datetime
from pony.orm import Database

db = Database()

class User(db.Entity):
    name = Required(str)
    phone_no = Required(str, unique=True, max_len=10)
    cars = Set('Car')

class Car(db.Entity):
    model = Required(str)
    color = Required(str)
    owner = Required(User) #userid
    purchase_date = Required(datetime) #'YYYY/MM/DD'
    services = Set('Servicing')

class Servicing(db.Entity):
    car = Required(Car)#car id
    servicing_date = Required(datetime)
    status = Required(str)