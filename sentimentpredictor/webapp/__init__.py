""" __init__.py will define the directory that contains it (webapp) as a package, that is why you
    can do things like : from webapp import routes,models
    NOTICE: This file can be easily REUSED just like it is, in many projects
"""

""" Basic FLASK support """
from flask import Flask, request
""" a config.py file is expected to have been set up in the previous filesystem directory
    a Config object must have been defined in that file ...
"""
from config import Config
""" Application Logging Support"""
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

""" Creating a FLASK application. """
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    """ REGISTERING all our application modules """
    from webapp.restapi import bp as restapi_bp
    app.register_blueprint(restapi_bp, url_prefix='/sentimentpredictor')

    """ For FILESYSTEM LOGGING will me made should we are neither in DEBUG nor TESTING modes """

    if not app.debug and not app.testing :
        if not os.path.exists('logs'):
            os.mkdir('logs')
        """ LOG files will be 10 KB each, they will rotate, keeping only the most recent 10 files """
        file_handler = RotatingFileHandler('logs/restapi.log', maxBytes=10240,backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('ML RESTAPI startup')

    return app
