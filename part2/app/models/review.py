from app.models.basemodel import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()
        if self.validate_text(text):
            self.text = text
        if self.validate_rating(rating):
            self.rating = rating
        if isinstance(place, Place):
            self.place = place
        if isinstance(user, User):
            self.user = user

    @staticmethod
    def validate_text(text):
        if not text:
            raise TypeError("Empty review")
        if type(text) is not str:
            raise TypeError("Review not valid")
        return True

    @staticmethod
    def validate_rating(rating):
        if rating > 0 or rating < 6:
            return True
        else:
            raise ValueError("Rating must be between 1 and 5")
