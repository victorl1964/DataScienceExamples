from flask import Blueprint

"""This is how we define 'main' dir as a module """
bp = Blueprint('restapi', __name__)

from webapp.restapi import routes
