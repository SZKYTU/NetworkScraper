from flask import Flask
from flask_restful import Api, Resource, fields, marshal

import json
from dbmodule import get

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return get()[0][0]

api.add_resource(HelloWorld, '/ip')

if __name__ == '__main__':
    app.run(debug=True)
