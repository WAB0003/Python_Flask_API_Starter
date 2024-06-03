# Starter Flask-SQLAlchemy API

## Server
### Create Virtual Environment
According to the [Flask Installation Docs](https://flask.palletsprojects.com/en/3.0.x/installation/), a virtual environment should always be used to manage the dependencies for project in both development and in production. 

Python comes with venv modules to create virtual environments automatically:
```
mkdir myproject
cd myproject
python -m venv .venv
```

This runs the venv modules and creates a directory *.venv*. To run the virtual environment, run the following in the terminal:

```
.\.venv\Scripts\activate
```

### Download Dependencies
For my basic starter api, the following dependencies are required:
```
pip install Flask
pip install Flask-Cors
pip install Flask-Migrate
<!-- pip install Flask-RESTful -->
pip install Flask-SQLAlchemy
pip install SQLAlchemy-serializer

pip install random2
pip install ipdb
```

Now that all dependency libraries have been downloaded, it's time to start creating intial application documents for the server-side programming. 

FYI, to view a list of all these type ```pip list```

## Setting up Application
First, in your project directory, create a new directory for the server side code by typing the following into the terminal:
```
mkdir server
cd server
```
Now that you're in the server directory, create the following (4) python files:
- **config.py**
- **app.py**
- **models.py**
- **seed.py**

### CONFIG.PY
The *config.py* file is used to set up the configuration of your python flask application. In this case, we are using sqlite and flask-migrate. Type the following code into your *config.py* file

```
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Create a Flask App that uses SQLite
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy()
migrate = Migrate(app, db)

db.init_app(app)

```
This sets up the configuration that will be needed to create a SQLite database that utilizes Flask-SQLAlchemy for an ORM.

Resources:
- [Flask-SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/)
- [Flask-Migrate Docs](https://flask-migrate.readthedocs.io/en/latest/)

### MODELS.PY
Using SQLAlchemy, create models. As an example, write the following code:
```
from sqlalchemy_serializer import SerializerMixin

from config import db

class Coordinate(db.Model, SerializerMixin):
    __tablename__ = 'coordinates'
    
    id = db.Column(db.Integer, primary_key=True)
    x_position = db.Column(db.Integer)
    y_position = db.Column(db.Integer)
    z_position = db.Column(db.Integer)
```
By importing SerializerMixen module, you can serialize SQLAlchemy model instances. It allows you to use the to_dict() method and create serialized rules.

Resources:
- [SQLAlchemy-serializer Doc](https://pypi.org/project/SQLAlchemy-serializer/)

### APP.PY
Now create a Flask Application. At a minimum, you will need the following code:
```
from flask import Flask, request, make_response, jsonify, session
from config import app
from models import Coordinate

CORS(app)

if __name__ == '__main__':
    app.run(port=5555)
```
This will create use the configuration file to create a flask application and run on Local Port 5555. 

Now that the *app.py* has been created. The Database needs to be initialized. Run the following to set up database migration connection:
```
flask db init
```

This creates a **migrations** and **instance** folder. You can edit these perameters for alembic, but the next step is:

```
flask db migrate -m "Initial Migration"
flask db upgrade 
```

This will set up the tables as defined in the your Models.py file and create a new *app.db* file in the **instance** directory. 

### SEED.PY
Let's create some initial test data. For this example, I wrote the following program that adds (2) coordinates to my coordinates table:

```
from app import app
from models import db, Coordinate

from random import randint

def create_coordinates():
    Coordinate.query.delete()

    coordA = Coordinate(x_position=randint(1,100), y_position=randint(1,100), z_position=randint(1,100))
    coordB = Coordinate(x_position=randint(1,100), y_position=randint(1,100), z_position=randint(1,100))
    
    # db.session.add(coordA)
    
    db.session.add_all([coordA, coordB])
    db.session.commit()
    print('created a coordA & coordB in "coordinates" table')

    
if __name__ == '__main__':
    with app.app_context():
        create_coordinates()
```

## Create Routes
Now the application has been set up and the database is working. Let's create some routes in the application API to GET information. 

Add the following method in app.py:

```
# CREATE ROUTES
@app.route('/coordinates', methods=['GET'])
def trajectories():
    if request.method == 'GET':
               # return jsonify([trajectory.to_dict() for trajectory in all_trajectories])
        return make_response([coord.to_dict() for coord in Coordinate.query.all()])
```

## Run Application
Now that you've built a route and set up the database, lets run the api application and confirm it works correctly. 

make sure you're in the server directory and run ```python app.py```

You should beging running a development server on port 5555

if you type the following into your browser, you should get the (2) coordiates in your coordinates table:

[http://127.0.0.1:5555/coordinates](http://127.0.0.1:5555/coordinates)