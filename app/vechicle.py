import datetime
import uuid
from bson.objectid import ObjectId
from flask import request
from flask_restplus import Resource
from utils.dto import VehicleDto

from jwt.exceptions import InvalidTokenError, InvalidSignatureError
from werkzeug.exceptions import InternalServerError
from utils.errors import NoDataProvided
from utils.tasks import save_vehicle, update_vehicle
from database.db_one import Vehicle as  Automobile
from service.vehicle_service import store_vehicle, log_data,\
    revise_vehicle


api = VehicleDto.api
_vehicle_I = VehicleDto.vehicle_input
_vehicle_O = VehicleDto.vehicle_output

@api.route('/')
class Vehicle(Resource):

    @api.response(201, 'Vehicle-Model Sucessful Sucessful')
    @api.doc('Add A New Vehicle')
    @api.expect(_vehicle_I, validate=True)
    def post(self):

        data = request.get_json()
        # Check if data is present
        if data:
            
            try:
                x = 1 # To help determine the result of the update
                public_id = str(uuid.uuid4())
                data['public_id'] = public_id
                
                result = save_vehicle.delay(data)
                response = store_vehicle(data)
            except:
                x = 0
                raise InternalServerError

            finally:
                if x==0:
                    result = 'Fail'
                else:
                    result = 'Pass'
                activity = 'Tried inputting {a}-{b},{c}, into databse'.format(
                    a = data['vehicle_type'],
                    b = data['vehicle_make'], 
                    c = data['vehicle_make']
                )
                log_data(result, activity)

            return response
            
        else:
            raise NoDataProvided

    
    @api.response(200, 'Vehicle Sucessful Added')
    @api.doc('Get All Vehicles Details')
    @api.marshal_list_with(_vehicle_O, envelope='data')
    def get(self):

        output = []

        try:
            vehicles = Automobile.objects
            #output = vehicles.to_json()
            for data in vehicles:
                 output.append({
                   'id': data['public_id'],
                    'approved': data['approved'],
                    'vehicle_make': data['vehicle_make'],
                    'vehicle_model': data['vehicle_model'],
                    'vehicle_type': data['vehicle_type'],
                    'status': data['status']
                 })
            if  len(output) == 0:
                output.append({
                    'error': 'We probably went blind for a minute'
                })
        except:
            raise InternalServerError

        finally:
            if output:
                result = 'Success'
            else:
                result = 'Fail'
            activity = 'Tried getting all of the {0} present in the Collection'.format(
                vehicles.count()
            )
            log_data(result, activity)
        
        return output




@api.route('/<id>')
class VehicleDetails(Resource):
    
    @api.response(200, 'Vehicle Sucessful Added')
    @api.doc('Get All Vehicles Details')
    @api.marshal_with(_vehicle_O)
    def get(self, id):

        output = []

        try:
            key = id
            vehicle = Automobile.objects(public_id= key)
            for data in vehicle:
                 output.append({
                   'id': data['public_id'],
                    'approved': data['approved'],
                    'vehicle_make': data['vehicle_make'],
                    'vehicle_model': data['vehicle_model'],
                    'vehicle_type': data['vehicle_type'],
                    'status': data['status']
                 })

            if  len(output) == 0:
                output.append({
                    'error': 'Cant find the vehicle, try another'
                })
        except:
            raise InternalServerError

        finally:
            if output:
                result = 'Success'
            else:
                result = 'Fail'
            activity = 'Tried getting the detais of {} present in the Collection'.format(
                str(vehicle)
            )
            log_data(result, activity)
        
        return output



    @api.response(201, '<Vehicle Details> Sucessful updated')
    @api.doc('Update A exiating Vehicle')
    @api.expect(_vehicle_I, validate=True)
    def put(self,id):

        data = request.get_json()
        # Check if data is present
        if data:
            
            try:
                x = 1 # To help determine the result of the update
                key = id
                data['public_id'] = key
                update_vehicle.delay(data)
                response = revise_vehicle(data)
            except:
                x = 0
                raise InternalServerError

            finally:
                if x == 0:
                    result = 'Fail'
                else:
                    result = 'Sucess'
                activity = 'Tried updating {i} {a}-{b},{c}, into databse'.format(
                    i = key,
                    a = data['vehicle_type'],
                    b = data['vehicle_make'], 
                    c = data['vehicle_make']
                )
                log_data(result, activity)

            return response
            
        else:
            raise NoDataProvided

    
