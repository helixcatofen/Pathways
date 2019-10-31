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
    return redirect('/profiles_grid')


@app.route('/support_options')
def support_options():
    return render_template('')


@app.route('/profiles_grid')
def profiles_grid():
    return render_template('profiles_grid.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/login')
def login():
    return render_template('login.html')


# TODO needs donate page
# @app.route('/profile/donate')
# def donate():
#     return ""
