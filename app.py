""" Server for Traveling Customer Web App """
from __future__ import print_function
from flask import Flask, render_template, request, jsonify
from python.OptimalPath import OptimalPath
from python.RouteContext import RouteContext
from python.ClosingTimePath import ClosingTimePath

# Constants
APP = Flask(__name__)


@APP.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main page of site """
    if request.method == 'POST':
        print("got post")
        content = request.get_json()

        location_list = parse_request(content)
        list_of_id = id_parsing(content)

        solution_dictionary = {}

        optimal_path = OptimalPath()
        context = RouteContext(optimal_path)
        solution = context.compute_route(location_list)
        if solution == -1:
            solution_dictionary['path_found'] = False
            solution_dictionary['optimal'] = []
        else:
            solution_dictionary['path_found'] = True
            solution_dictionary['optimal'] = construct_optimal_response(content, solution[0], solution[1])

        closing_path = ClosingTimePath()
        context2 = RouteContext(closing_path)
        solution2 = context2.compute_route(list_of_id)
        solution_dictionary['closing_time'] = construct_closing_time_response(content, solution2)
        solution_dictionary['closed_stores'] = True if solution2[2] else False

        print(solution_dictionary)

        return jsonify(solution_dictionary)
    if request.method == 'GET':
        return render_template('index.html')

def parse_request(json_info):
    """
        Returns a list containing tuples of (latitude, longitude)
        Index 0 is the Latitude and Longitude of the starting location as specified in json_info
    """

    location_list = [(json_info['info']['start_loc']['lat'], json_info['info']['start_loc']['lng'])]
    for place_dictionary in json_info['info']['places']:
        location_list.append((place_dictionary['latLng']['lat'], place_dictionary['latLng']['lng']))

    return location_list

def id_parsing(json_info):
    """
        Returns a list containing the unique location id for each location
    """
    id_list=[]
    for place_dictionary in json_info['info']['places']:
        id_list.append(place_dictionary['id'])

    return id_list

def construct_optimal_response(json_info, route, total_time):
    """
        Given the json data from the server,
        return the location data for all locations in the right order.
    """
    response = {'total_time':total_time}

    places_in_order = []
    for i in route:
        if i == 0:
            lat_lng_dict = {}
            lat_lng_dict['lat'] = json_info['info']['start_loc']['lat']
            lat_lng_dict['lng'] = json_info['info']['start_loc']['lng']

            place = {'name': 'Start Location', 'latLng': lat_lng_dict}
            places_in_order.append(place)
        else:
            places_in_order.append(json_info['info']['places'][i - 1])

    response['path'] = places_in_order

    return response

def construct_closing_time_response(json_info, solution):
    """
        create appropriate dictionary for closing time solution
    """

    response = {}

    places_in_order = [{'name': 'Start Location', 'latLng': {'lat':json_info['info']['start_loc']['lat'], 'lng':json_info['info']['start_loc']['lng']}}]
    for i in solution[3]:
        places_in_order.append(json_info['info']['places'][i[0]])


    for i in solution[0]:
        places_in_order.append(json_info['info']['places'][i])

    places_in_order.append([{'name': 'Start Location', 'latLng': {'lat':json_info['info']['start_loc']['lat'], 'lng':json_info['info']['start_loc']['lng']}}])


    response['path'] = places_in_order

    return response





if __name__ == '__main__':
    APP.run(debug=True)
