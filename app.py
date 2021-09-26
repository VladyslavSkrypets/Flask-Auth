from __init__ import app, db
from flask import make_response, render_template
from auth.views import auth as auth_blueprint
from admin.views import admin as admin_blueprint
from user_profile.views import profile as profile_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(profile_blueprint, url_prefix='/user')
app.register_blueprint(admin_blueprint, url_prefix='/admin')


@app.errorhandler(404)
def not_found(error):
    return make_response(render_template('404.html'), 404)


@app.route("/")
def home():
    return render_template("home/home.html")


if __name__ == '__main__':
    app.run(port=3001)
