import markdown
import os

from flask import Flask
from flask_restful import Api
from api.devices import Devices
from waitress import serve

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    with open(os.getcwd() + '\README.md') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


serve(app, port=5000)
