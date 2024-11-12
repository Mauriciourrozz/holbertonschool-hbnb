from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from app.models.review import Review

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        review_data = api.payload
        new_review = facade.create_review(review_data)
        return {
            "id": new_review.id,
            "text": new_review.text,
            "rating": new_review.rating,
            "user_id": new_review.user_id,
            "place_id": new_review.place_id
        }

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        lista = []
        lista2 = facade.get_all_reviews()
        for i in lista2:
            serializar = i.serializar_reviews()
            lista.append(serializar)
        return marshal(lista, review_model)

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        new_review = facade.get_review(review_id)
        return marshal(new_review, review_model), 200


    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        review_data = api.payload
        review = facade.get_review(review_id)
        facade.update_review(review_id, review_data)
        return {'message': 'Review updated successfully'}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        review_data = facade.get_review(review_id)
        facade.delete_review(review_id)
        return {'message': 'Review deleted successfully'}, 200

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        reviews_list = facade.get_reviews_by_place(place_id)
        return marshal(reviews_list, review_model), 200