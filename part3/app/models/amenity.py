from app.models.baseclass import BaseModel
from app import db
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    __tablename__ = 'amenities'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    places = db.relationship('Place', secondary='place_amenities', back_populates='amenities', lazy=True)
   
    def __init__(self, name: str):
        super().__init__()
        if type(name) is str and len(name) <= 50:
            self.name = name


    def serializar_amenities(self):
        return {
            'id': self.id,
            'name': self.name
        }
