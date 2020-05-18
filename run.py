import unittest
from werkzeug.utils import cached_property
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from database.db_two import db

from app.factory import create_app
import app


app = create_app(celery=app.celery)
app.app_context().push()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()

@manager.command
def test():
    """ Runs the unit tests. """
    tests = unittest.TestLoader().discover('./test', pattern='test*.py')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if results.wasSuccessful():
        return 0
    return 0

if __name__ == '__main__':
    manager.run()
    