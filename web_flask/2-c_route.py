web framework
web_flask/0-hello_route.py


#!/usr/bin/python3

""" Starts a Flash Web Application """

from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def hello_hbnb():

    """ Prints a Message when / is called """

    return 'Hello HBNB!'


if __name__ == "__main__":

    """ Main Function """

    app.run(host='0.0.0.0', port=5000)


web_flask/1-hbnb_route.py


#!/usr/bin/python3

""" Starts a Flash Web Application HBNB"""

from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)

def hello_hbnb():

    """ Prints a Message when / is called """

    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)

def hbnb():

    """ Prints a Message when /hbnb is called """

    return 'HBNB'


if __name__ == "__main__":

    """ Main Function """

    app.run(host='0.0.0.0', port=5000)


web_flask/2-c_route.py


#!/usr/bin/python3

""" Starts a Flash Web Application C is FUN"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)

def hello_hbnb():

    """ Prints a Message when / is called """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)

def hbnb():

    """ Prints a Message when /hbnb is called """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)

def c_is_fun(text):

    """ Prints a Message when /c is called """

    return "C " + text.replace('_', ' ')


if __name__ == "__main__":

    """ Main Function """

    app.run(host='0.0.0.0', port=5000)
