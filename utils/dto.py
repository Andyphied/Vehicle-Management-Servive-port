from flask_restplus import Namespace, fields


class VehicleDto:
    api = Namespace('Vehicle', description='Manages vehicle Realted Services')
    vehicle_input = api.model('Vehicle',{
        'approved': fields.Boolean(default=False, description=("Indicates if a vehicle"
        "is approved or not"), example= True),
        'vehicle_make': fields.String(required=True, description='The brand or make of the vehicle', example= 'Toyota'),
        'vehicle_model': fields.String(required=True, description="The vehicle's model", example= 'Corolla 2018'),
        'vehicle_type': fields.String(required=True, description='The type of vehicle', example='Saloon'),
        'status': fields.String(required=True, description='The status of the vehicle processing', example='Pending')
    })
    vehicle_output = api.model('Vehicle',{
        'id': fields.String(required=True, description='The Vehicle Identity' ),
        'approved': fields.Boolean(required=True, description=("Indicates if a vehicle"
        "is approved or not"), example= True),
        'vehicle_make': fields.String(required=True, description='The brand or make of the vehicle', example= 'Toyota'),
        'vehicle_model': fields.String(required=True, description="The vehicle's model", example= 'Corolla 2018'),
        'vehicle_type': fields.String(required=True, description='The type of vehicle', example='Saloon'),
        'status': fields.String(required=True, description='The status of the vehicle processing', example='Pending')
    })



class LogeDto:
    api = Namespace('Log', description='Creation of States')
    log = api.model('Log',{
        'activity': fields.String(required=True, description='The action at each endpoints'),
        'result': fields.String(required=True, description='The success'),
        'timestamp': fields.DateTime(description='The Dateand Time perfomred')
    })