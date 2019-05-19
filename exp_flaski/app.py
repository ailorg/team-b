from flask import Flask, render_template, abort
from flask import Flask, render_template, abort, request
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
def hello():
    contents = WikiContent.query.all()
    return render_template("show_content.html", content=content)


@app.route("/<title>", methods=["POST"])
def post_content(title=None):
    if title is None:
        abort(404)
    content = db.query(WikiContent).filter_by(title=title).first()
    if content is None:
        content = WikiContent(title,
                              request.form["body"]
                              )
    else:
        content.body = request.form["body"]
        content.date = datetime.now()
    db.add(content)
    db.commit()
    return content.body

if __name__ == "__main__":
    app.run()
