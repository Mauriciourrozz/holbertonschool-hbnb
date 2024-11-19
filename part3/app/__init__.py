from datetime import timedelta
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()

jwt = JWTManager()

db = SQLAlchemy()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/', prefix="/api/v1")

    from app.api.v1.users import api as users_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.auth import api as login_ns

    # Register the users namespace
    api.add_namespace(users_ns, path='/users')
    api.add_namespace(amenities_ns, path='/amenities')
    api.add_namespace(places_ns, path='/places')
    api.add_namespace(reviews_ns, path='/reviews')
    api.add_namespace(login_ns, path='/auth')

    # Inicializar SQLAlchemy
    db.init_app(app)

    # Inicializar JWTManager
    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    

    return app
