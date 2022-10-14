#!/usr/bin/python3
"""
starts a Flask web application listening on 0.0.0.0 port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
	"""Displays 'Hello HBNB!'"""
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""Displays 'HBNB'."""
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
	"""Displays 'c ' followed by the value of <text>.
	replaces any underscores in <text> with slashes.
	"""
	return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
	"""displays 'python' followed by the value of <text>
	replaces any underscores in <text> with slashes.
	"""
	text = text.replace("_", " ")
	return "python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
	"""displays 'n is a number' only if n is an integer"""
	return "{} is a number".format(n)
if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
