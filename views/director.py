from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        d_object = director_service.get_all()
        result = DirectorSchema(many=True).dump(d_object)
        return result, 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid):
        d_object = director_service.get_one(uid)
        result = DirectorSchema(many=True).dump(d_object)
        return result, 200
