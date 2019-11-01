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


def query_db(key=None):
    url = "https://pjgf4yqxo7.execute-api.eu-west-3.amazonaws.com/default/hackBackend"

    querystring = {"TableName": "ciscodb"}

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "d3d4467a-b606-4b40-be72-eb297d6401ab"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    if key is None:
        return response.json()["Items"]
    else:
        for item in response.json()["Items"]:
            if item["user"]['S'] == key:
                return item


@app.route('/')
@app.route('/index')
def index():
    return redirect('/profiles_grid')


@app.route('/test')
def test():
    return render_template('index.html')


@app.route('/profiles_grid')
def profiles_grid():
    profiles = query_db()
    return render_template('profiles_grid.html', profiles=profiles)


@app.route('/profile/<name>')
def profile(name):
    profile = query_db(name)
    return render_template('profile.html', profile=profile)


@app.route('/login')
def login():
    return render_template('login.html')
