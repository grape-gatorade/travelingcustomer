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
        content = request.get_json()

        place_name_list=[]
        place_ids = []
        for place in content['info']:
        	place_name_list.append(place['name'])
        	place_ids.append(place['id'])

        optimal_route=OptimalPath()
        closing_time_route=ClosingTimePath()

        strategy_context=RouteContext(optimal_route)
        print (strategy_context.compute_route(place_name_list))


       # strategy_context=RouteContext(closing_time_route)
        #strategy_context.compute_route(place_ids)


        return jsonify({'response': 'dictionary'})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    APP.run(debug=True)
