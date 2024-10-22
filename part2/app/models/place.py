from basicmodel import BaseModel
from user import User

class Place(BaseModel):
    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User):
        super().__init__
        if self.validate_title(self.title):
            self.title = title
        if self.vaidate_description(self.description):
            self.description = description
        if self.validate_price(self.price):
            self.price = price
        if self.validate_latitude(self.latitude):
            self.latitude = latitude
        if self.validate_longitude(self.longitude):
            self.longitude = longitude
        if isinstance(owner, User):
            self.owner = owner

    @staticmethod
    def validate_title(title):
        if type(title) is not str:
            raise TypeError("Title not valid")
        if len(title) > 100:
            raise ValueError("Title cannot contain more than 100 characters")
        return title

    @staticmethod
    def validate_description(description):
        if type(description) is not str:
            raise TypeError("Description not valid")
        return description

    @staticmethod
    def validate_price(price):
        if type(price) is not float:
            raise ValueError("Error: Price not valid")
        if price < 0:
            raise ValueError("Price must be greater than 0")
        return price

    @staticmethod
    def validate_latitude(latitude):
        if type(latitude) is not float:
            raise TypeError("Latitude not valid")
        if latitude > 90.0 or latitude < -90.0:
            raise ValueError("Latitude not valid")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        if type(longitude) is not float:
            raise TypeError("Latitude not valid")
        if longitude > 90.0 or longitude < -90.0:
            raise ValueError("Latitude not valid")
        return longitude
