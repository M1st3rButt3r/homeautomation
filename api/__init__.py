from flask import Flask
from flask_restful import Api
import markdown;
import os;


from api.devices import Devices;

app = Flask(__name__)
api = Api(app)

api.add_resource(Devices, "/devices")

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md') as markdown_file:
        content = markdown_file.read();
        return markdown.markdown(content);
