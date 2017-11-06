""" Server for Traveling Customer Web App """
from __future__ import print_function
from flask import Flask, render_template, request, jsonify
from python.OptimalPath import OptimalPath
from python.ClosingTimePath import ClosingTimePath
from python.RouteContext import RouteContext

# Constants
APP = Flask(__name__)


@APP.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main page of site """
    if request.method == 'POST':
        print ("got post")
        content = request.get_json()

        location_list = parse_request(content)

        optimal_path = OptimalPath()
        context = RouteContext(optimal_path)
        solution = context.compute_route(location_list)

        print(solution)

        return jsonify(construct_response(content, solution[0], solution[1]))
    else:
        return render_template('index.html')

def parse_request(json_info):
    """
        Returns a list containing tuples of (latitude, longitude)
        Index 0 is the Latitude and Longitude of the starting location as specified in json_info
    """

    location_list = [(json_info['info']['start_loc']['lat'], json_info['info']['start_loc']['lng'])]
    for place_dictionary in json_info['info']['places']:
        location_list.append((place_dictionary['lat'], place_dictionary['lng']))
    return location_list

def construct_response(json_info, route, total_time):
    response = {'total_time':total_time}

    places_in_order = [ (json_info['info']['start_loc'] if i == 0 else json_info['info']['places'][i - 1]) for i in route]

    response['path'] = places_in_order

    return response


if __name__ == '__main__':
    APP.run(debug=True)
