#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Returns Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_s.lashes=False)
def cisfun(text):
    """
    Displays "C " followed by the value of the text variable with underscores replaced by spaces.
    """
    return f"C {text.replace('_', ' ')}"  # f-string for formatted string


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """
    Displays "Python ", followed by the value of the text variable (default is "is cool").
    """
    return f"Python {text.replace('_', ' ')}"  # f-string for formatted string


@app.route("/number/<int:n>", strict_slashes=False)
def imanumber(n):
    """
    Displays "{n} is a number" only if n is an integer (uses f-string for cleaner formatting).
    """
    return f"{n} is a number"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
