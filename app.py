from flask import Flask, render_template
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')

app = Flask(__name__)

def test_gmaps():
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                        "Parramatta, NSW",
                                        mode="transit",
                                        departure_time=now)
    print (directions_result)
                                    

@app.route('/')
def hello_world():
    test_gmaps()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

