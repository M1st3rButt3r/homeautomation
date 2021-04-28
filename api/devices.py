from flask_restful import Resource, abort, reqparse
class Devices(Resource):
    def get(self):
        
        return {"device": "1"}

    def post(self):
        return {"is done": "1"}
