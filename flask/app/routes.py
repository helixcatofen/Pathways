from app import app
from flask import redirect, render_template

"""
List of different pages:
login
choosing panel
grid view / profiles_grid
profile
"""


@app.route('/')
@app.route('/index')
def index():
    return redirect('/support_options')


@app.route('/support_options')
def support_options():
    return render_template('support_me.html', title='Support')


@app.route('/profiles_grid')
def profiles_grid():
    return ""


@app.route('/profile')
def profile():
    return ""


@app.route('/login')
def login():
    return ""


# TODO needs donate page
# @app.route('/profile/donate')
# def donate():
#     return ""
