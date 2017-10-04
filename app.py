#!/usr/bin/env python3

"""
Traveling Customer
"""

from flask import Flask, render_template
from flask_bower import Bower
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
#import requests

APP = Flask(__name__)
Bower(APP)
GoogleMaps(APP, key="AIzaSyBYD0slC7nqfD1uEZMjp2l-RBrkgtQi2cA")
##google places api key AIzaSyBmj27cQr6mXfWQivdc2N4qs-AvbYaddVI

@APP.route('/')
def index():
    """ route for index page """
    return render_template('index.html')

@APP.route('/currentlocation')
def currentlocation():
    """ route for currentlocation page """
    return render_template('currentlocation.html')

@APP.route("/mapview")
def mapview():
    """ creates maps obejects and routes to mapview page """
    # creating a map in the view
    print("running mapview")
    #search_url = "https://www.googleapis.com/geolocation/v1/geolocate"\
    #    + "?key=AIzaSyBYD0slC7nqfD1uEZMjp2l-RBrkgtQi2cA"
    #search_payload = {"key":"AIzaSyBYD0slC7nqfD1uEZMjp2l-RBrkgtQi2cA"}
    #search_req = requests.get(search_url)
    # search_json = search_req.json()
    # print(search_json)
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }
        ]
    )
    return render_template('mapview.html', mymap=mymap, sndmap=sndmap)

@APP.route('/hello')
def hello():
    """ route for hello page """
    return render_template('hello.html')

if __name__ == "__main__":
    APP.run(debug=True)
