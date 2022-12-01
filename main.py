from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with

from dbmodule import get

data = get()


app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self):
        return get()

api.add_resource(Main,  '/ip')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
