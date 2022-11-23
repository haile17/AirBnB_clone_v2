#!/usr/bin/python3

"""
starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/airbnb-onepage", strict_slashes=False)
def hello():
	"""returns a string at the root route"""
	return "Hello HBNB!"


if __name__ == "__main__":
	app.run(host='127.0.0.1', port='5000')

