""" Server for Traveling Customer Web App """
from __future__ import print_function
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify
from python.OptimalPath import OptimalPath
from python.RouteContext import RouteContext
from python.ClosingTimePath import ClosingTimePath
from python.DistancePath import DistancePath
from python.DefaultPath import DefaultPath
import googlemaps


# Constants
APP = Flask(__name__)


@APP.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main page of site """
    if request.method == 'POST':
        print("got post")
        content = request.get_json()
        print(content)

        location_list = parse_request(content)
        list_of_id = id_parsing(content)
        start_time = parse_start_time(content)
        print("!!!!!start_time ", start_time)

        """
            Here we begin computing routes to send in the JSON response

            Format of JSON Response:
            {
                closed_stores: bool,
                path_found: bool,
                paths: [
                    { path: [
                        ...
                        ], travel_time: int
                    },
                    { path: [
                        ...
                    ], travel_time: int
                    },
                    { path: [
                        ...
                        ], travel_time: int
                    },
                    { path: [
                        ...
                    ], travel_time: int
                    }
                ]
            }
        """

        solution_dictionary = {'paths':[]}

        # Optimal Path
        optimal_path = OptimalPath()
        context = RouteContext(optimal_path)
        solution = context.compute_route(location_list, start_time)
        if solution == -1:
            solution_dictionary['path_found'] = False
            solution_dictionary['paths'].append({'path': [], 'travel_time':-1})
        else:
            solution_dictionary['path_found'] = True
            path = construct_optimal_response(content, solution[0])
            optimal_travel_time = compute_travel_time(path, 'driving', start_time)
            solution_dictionary['paths'].append({'name' : 'Optimal Path','path': path, 'travel_time': optimal_travel_time})


        # Closing Time Path
        closing_path = ClosingTimePath()
        context2 = RouteContext(closing_path)
        solution2 = context2.compute_route(list_of_id, start_time)
        path_list = construct_closing_time_response(content, solution2)
        solution_dictionary['closed_stores'] = True if solution2[2] else False
        travel_time = -1 if not solution_dictionary['path_found'] else compute_travel_time(path_list, 'driving', start_time)
        solution_dictionary['paths'].append({'name' : 'Closing Time Path', 'path': path_list, 'travel_time': travel_time})


        # Distance Path
        distance_path = DistancePath()
        context3 = RouteContext(distance_path)
        solution3 = context3.compute_route(location_list, start_time)
        if solution == -1:
            solution_dictionary['paths'].append({'path': [], 'travel_time': -1})
        else:
            path = construct_optimal_response(content, solution3[0])
            distance_travel_time = -1 if not solution_dictionary['path_found'] else compute_travel_time(path, 'driving', start_time)
            solution_dictionary['paths'].append({'name' : 'Distance Path', 'path': path, 'travel_time': distance_travel_time})

        # Default Path
        default_path = DefaultPath()
        context4 = RouteContext(default_path)
        solution4 = context4.compute_route(location_list, start_time)
        if solution == -1:
            solution_dictionary['paths'].append({'path': [], 'travel_time': -1})
        else:
            path = construct_optimal_response(content, solution4)
            default_travel_time = -1 if not solution_dictionary['path_found'] else compute_travel_time(path, 'driving', start_time)
            solution_dictionary['paths'].append({'name' : 'Default Path', 'path': path, 'travel_time': default_travel_time})

        return jsonify(solution_dictionary)
    if request.method == 'GET':
        return render_template('index.html')

def parse_start_time(json_info):
    """
        Determine if json contains start time info, if not use the current time.
    """

    start_time = 0
    try:
        start_time = json_info['info']['start_time']
        if start_time is None:
            start_time = datetime.now()
        else:
            depart_hour = start_time['hour']
            depart_minute = start_time['minute']
            depart_meridiem = start_time['meridiem']

            if depart_meridiem == 'PM':
                depart_hour += 12

            today = datetime.today()

            start_time = datetime(today.year, today.month, today.day, depart_hour, depart_minute)
            if start_time < datetime.now():
                start_time = datetime.now()
    except KeyError:
        start_time = datetime.now()

    extra_time = timedelta(minutes=5)

    start_time = start_time + extra_time

    print(start_time)
    return start_time

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
    id_list = []
    for place_dictionary in json_info['info']['places']:
        id_list.append(place_dictionary['id'])

    return id_list

def construct_optimal_response(json_info, route):
    """
        Given the json data from the server,
        return the location data for all locations in the right order.
    """
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

    return places_in_order

def construct_closing_time_response(json_info, solution):
    """
        create appropriate dictionary for closing time solution
    """
    places_in_order = [{'name': 'Start Location', 'latLng': {'lat':json_info['info']['start_loc']['lat'], 'lng':json_info['info']['start_loc']['lng']}}]
    for i in solution[3]:
        places_in_order.append(json_info['info']['places'][i[0]])


    for i in solution[0]:
        places_in_order.append(json_info['info']['places'][i])

    places_in_order.append({'name': 'Start Location', 'latLng': {'lat':json_info['info']['start_loc']['lat'], 'lng':json_info['info']['start_loc']['lng']}})

    return places_in_order

def compute_travel_time(path, travel_type='driving', start_time=None):
    """
        Given a list containing the path information,
        return the time to travel to each location from start to finish
    """
    if (start_time is None):
        start_time = datetime.now() + timedelta(minutes=5)

    gmaps = googlemaps.Client(key='AIzaSyBuGbc491h07Hp-ao-6o-dkLmUUX9OG_ho')

    total_time = 0

    for i in range(1, len(path)):
        dist_matrix = gmaps.distance_matrix((path[i - 1]['latLng']['lat'], path[i - 1]['latLng']['lng']),   # origin
                                            (path[i]['latLng']['lat'], path[i]['latLng']['lng']),      # destination
                                            travel_type,    # travel type
                                            'English',      # language
                                            None,           # things to avoid
                                            'imperial',     # units
                                            start_time, # departure time
                                            None,           # arrival time
                                            None,           # public transit
                                            None,           # transit preferences
                                            'best_guess')   # Traffic Model

        total_time += dist_matrix['rows'][0]['elements'][0]['duration']['value']

    return total_time

if __name__ == '__main__':
    APP.run(debug=True)
