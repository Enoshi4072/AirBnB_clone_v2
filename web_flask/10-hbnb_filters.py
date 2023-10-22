#!/usr/bin/env bash

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import environ

app = Flask(__name)

# This teardown method ensures that the SQLAlchemy session is closed after each request.
@app.teardown_appcontext
def close_db(error):
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    # Load states, cities, and amenities sorted by name (A->Z)
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
