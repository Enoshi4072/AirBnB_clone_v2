from flask import Flask, render_template
from models import storage
from models.state import State
from os import environ

app = Flask(__name)

# This teardown method ensures that the SQLAlchemy session is closed after each request.
@app.teardown_appcontext
def close_db(error):
    storage.close()

@app.route('/states', strict_slashes=False)
def list_states():
    # Fetch all states and sort them by name
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def state_info(id):
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
