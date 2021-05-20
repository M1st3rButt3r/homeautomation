from flask_restful import Resource, abort, reqparse


class DeviceAPI(Resource):
    def get(self, identifier):
        return {"message": "not implemented"}

    def post(self, identifier):
        parser = reqparse.RequestParser()

        parser.add_argument('action', required=True)

        args = parser.parse_args()

        return {"message": "not implemented"}

    def delete(self, identifier):
        return {"message": "not implemented"}
