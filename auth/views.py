from flask import Blueprint, render_template, make_response


auth = Blueprint('auth', __name__, template_folder='templates/auth')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    return make_response(render_template("login.html"), 200)


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    return make_response(render_template("signup.html"), 200)
