""" Server for Traveling Customer Web App """
from datetime import datetime
from flask import Flask, render_template
import test
import googlemaps

# Constants
GMAPS = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')
APP = Flask(__name__)

def test_gmaps():
    """ Testing out the Google Maps API """
    now = datetime.now()
    directions_result = GMAPS.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)
    print(directions_result)
    
@APP.route('/')
def hello_world():
    """ Main page of site """
    test_gmaps()
    return render_template('index.html')


if __name__ == '__main__':
    test.test_strategy()

    APP.run(debug=True)
