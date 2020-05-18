from flask import Blueprint
from flask_restplus  import Api
from .vechicle import api as vehicle_ns


api_bp = Blueprint('api', __name__)

api = Api(api_bp,
    title = 'Vehicles Backend Api',
    version = '0.10',
    description = ("This Service would be responsible for the creation of Vehicles,"
                    "editing/updating of Vehicles, and Search For Vehicles.")
    
)

api.add_namespace(vehicle_ns, path='/me/vehicles')