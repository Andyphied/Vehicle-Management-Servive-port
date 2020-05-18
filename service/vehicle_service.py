import datetime

from database.db_two import db, Vehicle, Log
from utils.tasks import save_log
from sqlalchemy import update


def store_vehicle(data):

    new_vehicle = Vehicle(
                    approved = data['approved'],
                    vehicle_make = data['vehicle_make'],
                    vehicle_model = data['vehicle_model'],
                    vehicle_type = data['vehicle_type'],
                    status = data['status'],
                    ref_id = data['public_id']
                )

    db.session.add(new_vehicle)
    db.session.commit()

    response = {
        'status': 200,
        'message': '{0} - {1} sucessfully registered'.format(
            data['vehicle_make'], 
            data['vehicle_model']),
        'id': data['public_id']
    }
    return response
    
def log_data(result, activity):

    log_dat ={
        'activity': activity,
        'result' : result,
        'timestamp': datetime.datetime.now()
    }
    save_log.delay(log_dat)
    
    new_log = Log(
        activity= activity,
        result= result,
        timestamp = log_dat['timestamp']
    )

    db.session.add(new_log)
    db.session.commit()



def revise_vehicle(data):
    key = (data['public_id'])
    Vehicle.query.filter_by(ref_id = key).update({
            Vehicle.status : data['status'],
            Vehicle.vehicle_make: data['vehicle_make'],
            Vehicle.vehicle_model: data['vehicle_model'],
            Vehicle.vehicle_type: data['vehicle_type'],
            Vehicle.approved: data['approved']
        })
    db.session.commit()


    response = {
        'status': 201,
        'message': '{0} - {1} sucessfully updated'.format(
            data['vehicle_make'], 
            data['vehicle_model']),
        'id': key
    }

    return response