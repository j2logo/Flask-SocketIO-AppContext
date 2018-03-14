from flask.json import jsonify
from flask_restful import Api, Resource

from . import api_bp

api = Api(api_bp)


class HelloWorldResource(Resource):

    def get(self):
        return jsonify({"hello": "world"})


api.add_resource(HelloWorldResource, '/api/hello/')
