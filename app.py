#!/usr/bin/env python3

"""
Traveling Customer
"""

from flask import Flask
APP = Flask(__name__)

@APP.route("/")
def hello_world():
    """
    Placeholder route
    """
    return "Hello, world!"

if __name__ == "__main__":
    APP.run()
