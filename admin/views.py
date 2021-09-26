from flask import Blueprint, render_template, make_response


admin = Blueprint('admin', __name__, template_folder='templates/admin')


@admin.route('/')
def index():
    return make_response(render_template("login.html"), 200)
