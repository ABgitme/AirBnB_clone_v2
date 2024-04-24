#!/usr/bin/python3
"""
This module defines a Flask web application with several routes
handling different URL patterns.

The application listens on network interface 0.0.0.0
and port 5000 by default.
"""
from flask import Flask, render_template

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


# defines the application routes for /number/<int>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route handler for the /number/<n> route.

    Args:
        n (int): The integer variable from the URL.

    Returns:
        str: A message indicating that n is a number.
    """
    return f'{n} is a number'


# defines the application routes for /number_template/<int:n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the /number_template/<n> route.

    Args:
        n (int): The integer variable from the URL.

    Returns:
        str: A HTML page with "Number: n" inside the <h1> tag.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for the /number_odd_or_even/<n> route.

    Args:
        n (int): The integer variable from the URL.

    Returns:
        str: A HTML page with "Number: n is even|odd" inside the <h1> tag.
    """
    if n % 2 == 0:
        evenorodd = 'even'
    else:
        evenorodd = 'odd'

    return render_template('6-number_odd_or_even.html',
                           n=n, evenorodd=evenorodd)


if __name__ == '__main__':
    """
    starts flack server
    listen on network 0.0.0.0:5000
    """
    app.run(host='0.0.0.0', port=5000)
