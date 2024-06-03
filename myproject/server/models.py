from sqlalchemy_serializer import SerializerMixin
# This allows you to serialize SQLAlchemy model information and use the to_dict() method:

from config import db

# You can have multiple Model Classes
class Coordinate(db.Model, SerializerMixin):
    __tablename__ = 'coordinates'
    # Rules for serialization that you DO NOT want in the response:
    serialize_rules =   (
                        "-created_at", 
                        "-updated_at",
                        )
    
    # Create (4) columns to the coordinates table in the db instance
    id = db.Column(db.Integer, primary_key=True)
    x_position = db.Column(db.Integer)
    y_position = db.Column(db.Integer)
    z_position = db.Column(db.Integer)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    # RELATIONSHIP PROPERTY EXAMPLES:
    # other_table_id = db.Column(db.Integer, db.ForeignKey("othertablename.id"))
    
    # DEFINE RELATIONSHIP EXAMPLES FOR SERIALIZATION:
    # property_name = db.relationship("Other_Class", back_populates="other_table")
    # property_name = db.relationship("Other_Class", back_populates="other_table", cascade="all, delete-orphan")
    
    # HOW YOU MAY WANT TO DISPLAY INFORMATION
    # def __repr__(self):
    #         return f'<Route {self.name}>'