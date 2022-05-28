from flask import Flask
from flask_restful import Api, Resource, request

app = Flask(__name__)
api = Api(app)


class Initialize(Resource):
    def get(self):
        return {'message': 'Initialize App Successfully'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
