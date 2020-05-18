import os
from  celery import Celery


def make_celery(app_name=__name__):
    return Celery(
        app_name, 
        backend = 'rpc://', 
        broker= os.getenv('CELERY_RESULT_URL')
        )

celery = make_celery()