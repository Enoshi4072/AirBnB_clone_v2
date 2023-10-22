#!/usr/bin/env bash
"""
starts a Flask web application listening on 0.0.0.0, port 5000
Using storage to fetch data from the storage engine
Loads all cities of a state
Routes:
    /hbnb_filters: display a HTML page.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name)

# This teardown method ensures that the SQLAlchemy session is closed after each request.
@app.teardown_appcontext
def close_db(error):
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    # Load states, cities, and amenities sorted by name (A->Z)
    states = storage.all("State")
    cities = storage.all("Cities")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
