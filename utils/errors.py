from werkzeug.exceptions import HTTPException

class NoDataProvided(HTTPException):
    code = 404
    description = 'No Request failed Because No Data Was Provided'