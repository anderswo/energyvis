from flask import Flask
from flask import request
from flask import render_template

from config import configure_app
from utils import get_instance_folder_path

print('Creating Flask instance...')
app = Flask(__name__, instance_path=get_instance_folder_path(),
            instance_relative_config=True)

print('Loading config file...')
configure_app(app)
app.logger.info('Created flask instance')
app.logger.info('Loaded config file')

print('Importing package relations (app, api, views, models)...')
app.logger.info('Importing package relations (app, api, views, models)...')
from app import views
from app import demo  # Demo views
from app import api
from app.database import db_session
from app import models


@app.errorhandler(404)
def page_not_found(error):
    # log route error
    app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('500.html'), 500
