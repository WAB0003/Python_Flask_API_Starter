from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Create a Flask App that uses SQLite
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Create a db instance using SQLAlchemy API
db = SQLAlchemy() # https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

# Use Flask-Migrate extension to handle migrations between for you app & db instance.
migrate = Migrate(app, db) # https://flask-migrate.readthedocs.io/en/latest/

db.init_app(app) # initialize application