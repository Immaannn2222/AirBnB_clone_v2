#!/usr/bin/python3
"""flask"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def handle(db):
    """handle"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def show_city():
    """cities"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
