#!/usr/bin/python3
"""
    starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


# defines the application routes
@app.route('/', strict_slashes=False)
def hello():
    """
    Displays a greeting message when the root URL is accessed.

    Returns:
        str: A greeting message, "Hello HBNB!".
    """
    return "Hello HBNB!"


# defines the application routes
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" on the /hbnb route.

    Returns:
        str: A message.
    """
    return 'HBNB'


if __name__ == '__main__':
    """
    starts flack server
    listen on network 0.0.0.0:5000
    """
    app.run(host='0.0.0.0', port=5000)
