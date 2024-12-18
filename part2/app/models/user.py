import re
from app.models.basemodel import BaseModel

class User(BaseModel):
    def __init__(self, first_name: str, last_name: str, email: str, is_admin=False):
        super().__init__()
        if self.validate_first_name(first_name) and self.validate_last_name(last_name):
            self.first_name = first_name
            self.last_name = last_name
        if self.validate_email(email):
            self.email = email
        self.is_admin = is_admin

    @staticmethod
    def validate_first_name(first_name):
        if type(first_name) is not str:
            raise TypeError("Name not valid")
        if len(first_name) > 50:
            raise ValueError("Name cannot contain more than 50 characters")
        return True

    @staticmethod
    def validate_last_name(last_name):
        if type(last_name) is not str:
            raise TypeError("Name not valid")
        if len(last_name) > 50:
            raise ValueError("Name cannot contain more than 50 characters")
        return True

    @staticmethod
    def validate_email(email):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, email):
            return True
        else:
            raise TypeError("Email not valid")

    def serializar_usuario(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
