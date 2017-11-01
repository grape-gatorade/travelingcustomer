""" Server for Traveling Customer Web App """
from __future__ import print_function
from flask import Flask, render_template, request, jsonify
from python.OptimalPath import OptimalPath
from python.RouteContext import RouteContext 

# Constants
APP = Flask(__name__)

@APP.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main page of site """
    if request.method == 'POST':
        content = request.get_json()

        place_list=[]
        for place in content['info']:
        	place_list.append(place['name'])

        optimal_route=OptimalPath()
        strategy_context=RouteContext(optimal_route)
        print (strategy_context.compute_route(place_list))



        




        return jsonify({'response': 'dictionary'})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    APP.run(debug=True)
