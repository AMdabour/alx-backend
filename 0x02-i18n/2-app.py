#!/usr/bin/env python3
"""web app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """"config class for flask babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """the home page"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """returns the best locale of the user"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)