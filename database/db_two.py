from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

"""
Defining This Database:
    - Database 2: Postgre Database
With exactly two table, The Vechicle and Log Table.
"""

# Database 2

class Vehicle(db.Model):
    __tablename__ = "Vechicle"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_id = db.Column(db.String(150), unique=True)
    approved = db.Column(db.Boolean(50), default=False)
    vehicle_make = db.Column(db.String(100), nullable=False)
    vehicle_model = db.Column(db.String(100), nullable=False)
    vehicle_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), default='pending')


    def __repr__(self):
        return "<Vechicle '{}'>".format(self.vechicle_model + self.vechicle_make)



class Log(db.Model):
    __tablename__ = "Logs"

    activity = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(100), nullable= False)
    timestamp = db.Column(db.DateTime, primary_key=True)

    def __repr__(self):
        return "<Log '{}'>".format(self.date_time)