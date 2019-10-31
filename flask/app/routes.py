from app import app
from flask import redirect, render_template
import requests

"""
List of different pages:

login
choosing panel
grid view / profiles_grid
profile
"""


def query_db():
    url = "https://pjgf4yqxo7.execute-api.eu-west-3.amazonaws.com/default/hackBackend"

    querystring = {"TableName": "ciscodb"}

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "d3d4467a-b606-4b40-be72-eb297d6401ab"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()["Items"][0]


@app.route('/')
@app.route('/index')
def index():
    return redirect('/profiles_grid')


@app.route('/support_options')
def support_options():
    return render_template('')


@app.route('/profiles_grid')
def profiles_grid():
    profiles = query_db()
    return render_template('profiles_grid.html', profiles=profiles)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/login')
def login():
    return render_template('login.html')
