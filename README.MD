# VEHICLE MANAGEMENT SERVICE

To run this service the following nust be run done:


Open bash, terminal, cmd or whatever rocks your boat

To install the packages in this repo we use the packagemanger [pip] (https://pip.pypa.io/en/stable) to install pipenv
to replace it.

```bash
pip install pipenv
```
Then you move along to 

```bash
pipenv install
```
This installs all the dependemcies required, so next we:
Create a .env file with all of the settings in it, check out the /app/config.py and __init__.py you would see what you need to get.

After doing that we can then
```bash
celery worker -A celery_worker.celery --loglevel=info --pool=solo
```

The above step requires you either have a meassage queue server implemented, an example is Redis or Rabbitmq.
So we Move,


```bash
python run.py runserver
```
The above would startup up your server and you can acess the beautiful swagger UI documentaion at localhost/api

## Incase of An error:

Look for the *werkzeug* package in your virtual enviroment an edit two files, edit them as the error comes, replacing werkzeug import cached property with, from werkzeug.utils import cached_property

