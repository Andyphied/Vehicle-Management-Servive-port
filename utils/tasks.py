from app import celery
from database.db_one import Vehicle, Log

@celery.task()
def save_vehicle(data):
    return Vehicle(**data).save()

@celery.task()
def save_log(data):
    return Log(**data).save()

@celery.task()
def update_vehicle(data):
    return Vehicle(**data).save()