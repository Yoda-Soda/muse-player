from flask import Flask, request
from flask_restful import Resource, Api
import json
from flask_cors import CORS, cross_origin
from ytmusicapi import YTMusic


ytmusic = YTMusic('headers_auth.json')


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# @cross_origin()
class Employees(Resource):
    def get(self):
        return {'employees': 'hello employees'} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        result = {'data': 'Tracks'}
        return jsonify(result)

class Music_Search(Resource):
    def get(self, search):
        search_results = ytmusic.search(search)
        return search_results
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Music_Search, '/music/<search>') # Route_3



if __name__ == '__main__':
     app.run(port='5002')