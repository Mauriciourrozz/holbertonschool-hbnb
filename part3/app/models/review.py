from app.models.baseclass import BaseModel
from app import db
from sqlalchemy.orm import validates

class Review(BaseModel):

    __tablename__ = 'reviews'

    text = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='reviews', lazy=True)
    place = db.relationship('Place', back_populates='reviews', lazy=True)

    def __init__(self, text: str, rating: int, place_id , user_id):
        super().__init__()
        if self.validate_text(text):
            self.text = text
        if self.validate_rating(rating):
            self.rating = rating
        self.place_id = place_id
        self.user_id = user_id


    @staticmethod
    @validates('text')
    def validate_text(text):
        if not text:
            raise TypeError("Empty review")
        if type(text) is not str:
            raise TypeError("Review not valid")
        return True

    @staticmethod
    @validates('rating')
    def validate_rating(rating):
        if 1 <= rating <= 5:
            return True
        else:
            raise ValueError("Rating must be between 1 and 5")

    def serializar_reviews(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating
        }