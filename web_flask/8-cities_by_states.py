#!/usr/bin/python3
"""
Web App is listening on 0.0.0.0, port 5000
using storage to fetch data from the storage engine
Loads all cities of a state
Routes:
    /states: display a HTML page:
    /states/<id>: display a HTML page
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    # Fetch all states and sort them by name
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)

# This teardown method ensures that the SQLAlchemy session is closed after each request.
@app.teardown_appcontext
def teardown(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
