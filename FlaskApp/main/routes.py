from flask import render_template, request, Blueprint
from FlaskApp.apps.Employees import routes
from FlaskApp.apps.Posts import routes
main = Blueprint('main', __name__)
