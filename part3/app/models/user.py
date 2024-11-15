import re
from app.models.basemodel import BaseModel
from flask_bcrypt import bcrypt, Bcrypt
from app import db, bcrypt
import uuid
from .base_model import BaseModel

bcrypt = Bcrypt()

class User(BaseModel):
    __tablename__ = 'users'

     first_name = db.Column(db.String(50), nullable=False) #String y notNull
     last_name = db.Column(db.String(50), nullable=False) #String y notNull
     email = db.Column(db.String(120), nullable=False, unique=True) #String, notNull y único
     password = db.Column(db.String(128), nullable=False) #String y notNull
     is_admin = db.Column(db.Boolean, default=False) #Boolean y False por defecto
    
    def serializar_usuario(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }

    def hash_password(self, password):
        """Hashes the password before storing it."""
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
    