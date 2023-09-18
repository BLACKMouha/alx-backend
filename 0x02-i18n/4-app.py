#!/usr/bin/env python3
'''1-app module'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, Locale

app = Flask(__name__)
babel = Babel(app)


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
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
