import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

from flask_bootstrap import Bootstrap
Bootstrap(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '537c78f0d4da40096e148f45be62883a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flask:flask@db/flask'
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from FlaskApp.main import routes
