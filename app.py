""" Server for Traveling Customer Web App """
from __future__ import print_function
from flask import Flask, render_template, request, jsonify

# Constants
APP = Flask(__name__)

@APP.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main page of site """
    if request.method == 'POST':
        content = request.get_json()
        print(content)
        return jsonify({'response': 'dictionary'})
    else:
        return render_template('index.html')


if __name__ == '__main__':
    APP.run(debug=True)
