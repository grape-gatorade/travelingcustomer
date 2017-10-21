from flask import Flask, render_template
import json
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')

app = Flask(__name__)

def test_gmaps():
    
    matrix=gmaps.distance_matrix(["Wal-Mart, Troy, NY", "Rensselaer Polytechnic Institute"], ["Wal-Mart, Troy, NY", "Rensselaer Polytechnic Institute"],
                    "driving", "English", None, "imperial",
                    datetime.now(), None, "driving",
                    None, None)


    x=matrix["rows"][0]["elements"][1]
    print json.dumps(x)

                                    

@app.route('/')
def hello_world():
    test_gmaps()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

