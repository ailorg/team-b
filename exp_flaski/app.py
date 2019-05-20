from flask import Flask, render_template, abort, request, jsonify
from flaski.models import WikiContent
from flaski.database import db
from datetime import datetime

import os
import json
import sys

env = os.getenv("APP_ENV", "local")
app = Flask(__name__)
app.config.from_pyfile("config/{}.properties".format(env))


@app.teardown_request
def shutdown_session(exception=None):
    db.remove()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<class_name>", methods=["GET"])
def post_content(class_name=None):
    if class_name is None:
        abort(404)
    content = db.query(WikiContent).filter_by(class_name=class_name).first()
    if content is None:
        return "NO DATA"
    else:
        return jsonify(class_name=content.class_name,
                       teacher = content.teacher,
                       text = content.text)

if __name__ == "__main__":
    app.run()
