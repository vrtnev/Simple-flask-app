from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Simple flask app by vrtnev"

@app.route("/<input>")
def hello(input):
    return f"Hello, {input}!"