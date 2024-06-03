from app import app
from models import db, Coordinate

from random import randint
import ipdb

def create_coordinates():
    # Delete database Table if it already exists
    Coordinate.query.delete()
    print('deleted table')
    coordA = Coordinate(x_position=randint(1,100), y_position=randint(1,100), z_position=randint(1,100))
    coordB = Coordinate(x_position=randint(1,100), y_position=randint(1,100), z_position=randint(1,100))
    
    # db.session.add(coordA)
    
    db.session.add_all([coordA, coordB])
    db.session.commit()
    print('created a coordA & coordB in "coordinates" table')
    # ipdb.set_trace()
    
if __name__ == '__main__':
    with app.app_context():
        create_coordinates()