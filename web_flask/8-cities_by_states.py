#!/usr/bin/env bash
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import environ

app = Flask(__name)

# This teardown method ensures that the SQLAlchemy session is closed after each request.
@app.teardown_appcontext
def close_db(error):
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    # Fetch all states and sort them by name
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
