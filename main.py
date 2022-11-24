from flask import Flask
from flask_restful import Resource, Api
from scrap import IP

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': f'{IP}'}

api.add_resource(HelloWorld, '/ip')

if __name__ == '__main__':
    app.run(debug=True)
