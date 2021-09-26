from flask import Flask
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
config = dotenv_values(".env")
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config['USERNAME']}:{config['PASSWORD']}@localhost/{config['DATABASE']}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)
