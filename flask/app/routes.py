from app import app
from flask import redirect, render_template
import requests
import json

"""
List of different pages:

login
choosing panel
grid view / profiles_grid
profile
"""


def query_db(key=None, secondary_key=None):
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
    elif key is not None and secondary_key is None:
        for item in response.json()["Items"]:
            if item["user"]['S'] == key:
                return item
    elif key is not None and secondary_key is not None:
        for item in response.json()["Items"]:
            if item["user"]["S"] == key:
                for goal in item["goals"]["L"]:
                    if goal["M"]["title"]["S"] == secondary_key:
                        return goal["M"]
    else:
        return None


def send_message(name):
    url = "https://api.ciscospark.com/v1/messages"

    payload = {
        "toPersonEmail": "mario.l.geuenich@gmail.com",
        "text": "Hi " + name + " my name is Anna, I would like to help you in your path to a job. "
                               "Should we set up a meeting soon? I am available every Wednesday."
    }
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer NDA0OTZiYmYtNDMwZC00N2E1LWEwZTUtMGViYjkzYTA5MmYwYmQ0NWRmNmItNjU1_PF84_55b3cabf-52c4-405d-916d-dee2f1741e18",
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

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)


def update_db(name, amount):
    url = "https://pjgf4yqxo7.execute-api.eu-west-3.amazonaws.com/default/hackBackend"

    payload = {
        "TableName": "ciscodb",
        "Key": {"user": {
            "S": "John"
        }
        },
        "UpdateExpression": "set goals[0].currAmount = goals[0].currAmount + :val",
        "ExpressionAttributeValues": {":val": {"N": "10"}}
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "cc469354-b6fc-4b81-9bfb-437d04f4ec36"
    }

    response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

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
    profile = query_db(key=name)
    return render_template('profile.html', profile=profile)


@app.route('/mentees')
def mentees():
    profiles = query_db()[:2]
    print(profiles)
    return render_template('mentees.html', profiles=profiles)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/donate/<name>')
def donate(name):
    profile = query_db(key=name)
    print(profile)
    return render_template('donations.html', profile=profile)


@app.route('/call_chat_api/<name>')
def call_chat_api(name):
    send_message(name)
    return redirect('https://teams.webex.com/')


@app.route('/payment/<name>/<donation>')
def payment(name, donation):
    goal = query_db(key=name, secondary_key=donation)
    return render_template('payment.html', goal=goal)
