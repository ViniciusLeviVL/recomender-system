from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!", 200

@app.route("/json")
def hello_main():
    a = "teste"
    return jsonify({
      "teste": a
    }), 200