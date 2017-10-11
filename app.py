#!/usr/bin/env python3

"""
Traveling Customer
"""

from flask import Flask
from flask_bower import Bower

APP = Flask(__name__, static_folder='public', static_url_path='/static')
Bower(APP)

@APP.route("/")
def hello_world():
    """
    Placeholder route
    """
    return "Hello, world!"

if __name__ == "__main__":
    APP.run()
