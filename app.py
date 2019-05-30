from flask import Flask, request, render_template, jsonify
app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
@app.route("/api", methods=['POST'])
# /apiにPOSTでデータを送りつけると、送られたフォームデータをsplit()したものをjsonで返します
def return_json():
    result = {
        "results": request.json["text"].split()
    }
    return jsonify(result)

