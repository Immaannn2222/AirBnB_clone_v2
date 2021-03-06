#!/usr/bin/python3
"""flask"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hi():
    """say hi"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def another_one():
    """route 2"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """third"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
