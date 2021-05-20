import markdown
import os

from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api
from api.devices import DevicesAPI
from api.device import DeviceAPI
from waitress import serve


app = Flask(__name__)
api = Api(app)

api.add_resource(DevicesAPI, "/devices")
api.add_resource(DeviceAPI, "/device/<string:identifier>")

@app.route("/")
def index():
    with open(os.getcwd() + '\README.md') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


serve(app, port=5000)
