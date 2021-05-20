from flask_restful import Resource, abort, reqparse


class DevicesAPI(Resource):
    def get(self):
        return {"message": "not implemented"}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True)
        parser.add_argument('type', required=True)
        parser.add_argument('gateway', required=True)

        args = parser.parse_args()

        return {"message": "not implemented"}
