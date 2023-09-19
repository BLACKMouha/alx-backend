#!/usr/bin/env python3
'''1-app module'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, Locale, format_datetime
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    '''Config representation for setting a Flask app'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    '''Finds the best choice from the set of supported languag'''
    lang = request.args.get('locale', None)
    app_langs = app.config.get('LANGUAGES', ['en', 'fr'])
    if lang in app_langs:
        return Locale(language=lang)
    if g.user:
        lang = g.user.get('locale', None)
        if lang in app_langs:
            return lang
    lang = request.headers.get('locale', None)
    if lang in app_langs:
        return lang
    return request.accept_languages.best_match(
        app.config.get('LANGUAGES', ['en', 'fr']))


@babel.timezoneselector
def get_timezone():
    '''Gets the timezone base on a priority scheme'''
    tz = request.args.get('timezone', None)
    if tz:
        try:
            return pytz.timezone(tz).zone
        except pytz.exceptions.UnknownTimeZoneError as utze:
            print(utze)

    if g.user:
        try:
            tz = g.user.get('timezone')
            return pytz.timezone(tz).zone
        except pytz.exceptions.UnknownTimeZoneError as utze:
            print(utze)
    return app.config.get('BABEL_DEFAULT_TIMEZONE', None)


@app.route('/', strict_slashes=False)
def index():
    '''Handle root route'''
    current_datetime = format_datetime(
        datetime.now(tz=pytz.timezone(get_timezone())))
    return render_template(
        '7-index.html',
        current_datetime=current_datetime)


@app.before_request
def before_request():
    '''Called before handling a request'''
    g.user = get_user()


def get_user():
    '''Returns a user dictionary based on the ID passed to the login_as URL
    argument.
    '''
    uID = request.args.get('login_as', None)
    if uID:
        try:
            return users.get(int(uID), None)
        except Exception as e:
            print('a number should be given')
            return None
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
