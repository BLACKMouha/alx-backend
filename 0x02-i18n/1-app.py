#!/usr/bin/env python3
'''1-app module'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, get_locale, get_timezone
from pytz import utc

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Config representation for setting a Flask app'''
    LANGUAGES = ['en', 'fr']
    locale = 'en'
    timezone = 'UTC'


config = Config()
app.config['BABEL_DEFAULT_LOCALE'] = config.locale
app.config['BABEL_DEFAULT_TIMEZONE'] = config.timezone


@babel.localeselector
def get_locale():
    return config.locale


@babel.localeselector
def get_timezone():
    return config.timezone


@app.before_request
def before_any_request():
    '''Called before a request is handled'''
    g.locale = str(get_locale())
    g.timezone = str(get_timezone())


@app.route('/', strict_slashes=False)
def index():
    '''Handle root route'''
    return render_template('1-index.html'), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
