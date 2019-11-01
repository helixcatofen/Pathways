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


def send_message(name):
    url = "https://api.ciscospark.com/v1/messages"

    payload = "{\n  \"toPersonEmail\": \"mario.l.geuenich@gmail.com\",\n  \"text\": \"Hi there\"\n}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer ZDdjYmY0NmUtYmU0My00ZGM2LWEwYjYtMDQxMzVlOTE5ZGE2NGNlYzI5NTctYjA5_PF84_55b3cabf-52c4-405d-916d-dee2f1741e18",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a4ad859b-fc2e-464c-92d0-c8fbd95a6769,d593a558-15a0-4f39-a4c7-c2fc2cc25e0a",
        'Host': "api.ciscospark.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "73",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


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


@app.route('/call_chat_api/<name>')
def call_chat_api(name):
    send_message(name)
    return redirect('https://teams.webex.com/')
