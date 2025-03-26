from flask import Flask

app  = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>MPW LONDON $1000!</p>"