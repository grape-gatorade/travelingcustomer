""" Server for Traveling Customer Web App """
from datetime import datetime
from flask import Flask, render_template

# Constants
APP = Flask(__name__)
                                    
@APP.route('/')
def hello_world():
    """ Main page of site """
    return render_template('index.html')


if __name__ == '__main__':
    APP.run(debug=True)
