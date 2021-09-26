from flask import Blueprint, render_template, make_response


profile = Blueprint('user_profile', __name__, template_folder='templates/user_profile')


@profile.route('/profile')
def profile_page():
    return "profile"
