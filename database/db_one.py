from flask_mongoengine import MongoEngine

db = MongoEngine()

"""
Defining This Database:
    - Database 1: MongoDb Database
With exactly two table, The Log and Vehicle Table.
"""

class Vehicle(db.Document):
    approved = db.BooleanField(default=False)
    vehicle_make = db.StringField()
    vehicle_model = db.StringField()
    vehicle_type = db.StringField()
    status = db.StringField(default = 'pending')
    public_id = db.StringField()

class Log(db.Document):
    activity = db.StringField()
    result = db.StringField()
    timestamp = db.DateTimeField()