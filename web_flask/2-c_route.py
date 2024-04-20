#!/usr/bin/python3
"""
    starts a Flask web application
"""

from flask import Flask, escape

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
    return f'C {escape(text.replace("_", " "))}'


if __name__ == '__main__':
    """
    starts flack server
    listen on network 0.0.0.0:5000
    """
    app.run(host='0.0.0.0', port=5000)
