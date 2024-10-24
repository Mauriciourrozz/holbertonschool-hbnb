from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.models.user import User
from app.models.place import Place

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        place_data = api.payload
        
        new_place = facade.create_place(place_data)
        return {
          "title": new_place.title,
          "description": new_place.description,
          "price": new_place.price,
          "latitude": new_place.latitude,
          "longitude": new_place.longitude,
          "owner_id": #acceder al id del usuario
          #acceder a las amenities
        }

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        lista = []
        lista2 = facade.get_all_places()
        for i in lista2:
            serializado = i.serializar_places()
            lista.append(serializado)
        return lista


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(place_id)
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": #implementar owner, acceder a los id,
            "amenities": #implementar amenities
        }


    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        data = api.payload

        if not data["title"] or not data["description"] or not data["longitude"] or not data["latitude"] or not data["price"]:
            return {"error": "Missing data"}, 400
        place = facade.update(place_id, data)
        return {"message": "Place updated successfully"}, 200