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

class Artist(Resource):
    def get(self, channelId):
        artist_results = ytmusic.get_artist(channelId)
        return artist_results

class Music_Search(Resource):
    def get(self, search, filter):
        search_results = ytmusic.search(search, filter)
        return search_results
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Artist, '/artist/<channelId>') # Route_2
api.add_resource(Music_Search, '/music/<filter>/<search>') # Route_3



if __name__ == '__main__':
     app.run(port='4231')