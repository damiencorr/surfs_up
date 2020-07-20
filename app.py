
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route("/hello")
def hello():
    return "Hello 2 World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name#</string:name>

if __name__ == "__main__":
    app.run()