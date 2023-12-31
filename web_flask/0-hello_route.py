#!/usr/bin/python3
from flask import Flask
""" 
Starts a Flask web App
It is listening on 0.0.0.0, port 5000
Routes:
    /: display Hello 'HBNB'
"""
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
