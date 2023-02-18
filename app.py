from flask import Flask,render_template
import pandas as pd
import os

from config.config_files import APIkeys

api_key = APIkeys.api_key


def get_movie_suggestions():
    pass


app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    suggestions = get_movie_suggestions()
    return render_template('index.html',suggestions=suggestions)


if __name__ == '__main__':
    app.run(debug=True)