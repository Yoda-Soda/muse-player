from flask import Flask, request
from flask_restful import Resource, Api
# # from sqlalchemy import create_engine
# from json import dumps
# from flask.ext.jsonpify import jsonify
import json
from ytmusicapi import YTMusic
# import webbrowser
# from json import dumps
# import requests



ytmusic = YTMusic('headers_auth.json')
# search_results = ytmusic.search('Three nights')
# search_results = json(search_results)
# # song_id = search_results[0]
# song_id = [search_results[0]['videoId']]
# print(type(song_id))
# print(song_id)
# print(type(song_id[0]))
# print(song_id[0])

# app_json = json.dumps(search_results)
# print(app_json)







# webbrowser.open("https://www.youtube.com/watch?v=" + song_id[0] )



app = Flask(__name__)
api = Api(app)

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