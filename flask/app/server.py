from flask import Flask, session, request, jsonify, make_response, render_template
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import requests

import json
import sys
import os

from app.models.db_connector import DatabaseAccessor
from app.models.users import WikiContent


args = sys.argv
env = os.getenv("APP_ENV", "local")

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
app.config.from_pyfile("config/{}.properties".format(env))
api = Api(app, version='0.0.1', title='API', description='API')

app.secret_key = app.config['SECRET_KEY']
app.supports_credentials = True
CORS(app, resources={r"/*": {"origins": "*"}})

ns = api.namespace('api')

db = DatabaseAccessor.get_session(app.config)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
class Path(Resource):
    @staticmethod
    def catch_all(path):
        return render_template("index.html")

@api.route("/hello")
class Hello(Resource):

    @staticmethod
    def get():
        return {"Hello":"World!"}


@api.route("/<class_name>")
class Post_content(Resource):

    @staticmethod
    def get(class_name=None):
        if class_name is None:
            abort(404)
        content = db.query(WikiContent).filter_by(class_name=class_name).first()
        if content is None:
            return "NO DATA"
        else:
            return jsonify(class_name=content.class_name,
                       teacher = content.teacher,
                       text = content.text)

@api.route('/health')
class HealthCheck(Resource):

    @staticmethod
    def get():
        user = db.query(WikiContent).filter_by(class_name="math").first()
        if user:
            print(user.class_name)

        return jsonify({"status": "ok", "message": "this is message from Flask"})
