from flask import Flask, session, request, jsonify, make_response, render_template
from flask_cors import CORS
import requests

import json
import sys
import os

from app.models.db_connector import DatabaseAccessor
from app.models.users import WikiContent


args = sys.argv
env = os.getenv("APP_ENV", "local")

app = Flask(__name__, static_folder = "../../dist/static", template_folder = "../../dist")
app.config.from_pyfile("config/{}.properties".format(env))

app.secret_key = app.config['SECRET_KEY']
app.supports_credentials = True
CORS(app, resources={r"/*": {"origins": "*"}})

db = DatabaseAccessor.get_session(app.config)



@app.route("/")
def catch_all():
    return render_template("index.html")


@app.route("/<class_name>")
def get_class(class_name=None):
    if class_name is None:
        abort(404)
    content = db.query(WikiContent).filter_by(class_name=class_name).first()
    if content is None:
        return "NO DATA"
    else:
        return jsonify(class_name=content.class_name,
                       teacher = content.teacher,
                       text = content.text,
                       score = content.score)

@app.route('/health')
def get_health():
    user = db.query(WikiContent).filter_by(class_name="math").first()
    if user:
        print(user.class_name)

    return jsonify({"status": "ok", "message": "this is message from Flask"})
