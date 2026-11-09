from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)

api = Api(app)

app.config.from_object('src.config.DevelopmentConfig')


class Post(Resource):
    def get(self):
        return {
            "message": "Ping! Pong!",
            "status": "Success"
        }
    
api.add_resource(Post, '/ping')

