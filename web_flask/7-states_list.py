#!/usr/bin/python3
"""
Start a Flask web application listening on 0.0.0.0, port 5000
Uses storage for fetching data from the storahe engine
Routes:
    /states_list: display a HTML page: (inside the tag BODY
    H1 tag: “States"
    UL tag: with the list of all State objects
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from flask import g

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a list of states
    """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
