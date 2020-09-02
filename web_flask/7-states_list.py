#!/usr/bin/python3
"""flask"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from operator import getitem
app = Flask(__name__)


@app.teardown_appcontext
def handle(db):
    """handle"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def fetch():
    """fetch"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
