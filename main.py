from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with

import json
from dbmodule import get

resource_fields = {
    'IP': fields.String,
    'HN': fields.String,
    'status': fields.Integer,
}

data = get()


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        json.dumps(get()[0])

api.add_resource(HelloWorld,  '/ip')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
