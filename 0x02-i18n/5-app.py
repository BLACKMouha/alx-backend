#!/usr/bin/env python3
'''1-app module'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, Locale

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
    if lang:
        return Locale(language=lang)
    return request.accept_languages.best_match(
        app.config.get('LANGUAGES', ['en', 'fr']))


@app.route('/', strict_slashes=False)
def index():
    '''Handle root route'''
    return render_template('5-index.html')


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
