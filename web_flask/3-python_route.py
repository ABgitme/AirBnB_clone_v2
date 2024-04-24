#!/usr/bin/python3
"""
This module defines a Flask web application with several routes
handling different URL patterns.

The application listens on network interface 0.0.0.0
and port 5000 by default.
"""
from flask import Flask

app = Flask(__name__)


# defines the application routes /
@app.route('/', strict_slashes=False)
def hello():
    """
    Displays a greeting message when the root URL is accessed.

    Returns:
        str: A greeting message, "Hello HBNB!".
    """
    return "Hello HBNB!"


# defines the application routes for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" on the /hbnb route.

    Returns:
        str: A message.
    """
    return 'HBNB'


# defines the application routes for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the /c/<text> route.

    Args:
        text (str): The text variable from the URL.

    Returns:
        str: A message displaying 'C '
        followed by the value of the text variable.
    """
    return f'C {text.replace("_", " ")}'


# defines the application routes for /python/<text>
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    """
    Route handler for the /python/<text> route.

    Args:
        text (str, optional): The text variable
        from the URL. Defaults to "is_cool".

    Returns:
        str: A message displaying 'Python '
        followed by the value of the text variable.
    """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    """
    starts flack server
    listen on network 0.0.0.0:5000
    """
    app.run(host='0.0.0.0', port=5000)
