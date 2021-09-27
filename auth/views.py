from __init__ import db
from flask import Blueprint, render_template, make_response, request


auth = Blueprint('auth', __name__, template_folder='templates/auth', static_folder='static')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        pass
    return make_response(render_template("login.html"), 200)


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        pass
    return make_response(render_template("signup.html"), 200)
