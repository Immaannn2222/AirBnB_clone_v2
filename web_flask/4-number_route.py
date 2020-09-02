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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth_func(text='is cool'):
    """fourth route"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_int(n):
    """is it an integer"""
    return '%d is a number' % n


if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
