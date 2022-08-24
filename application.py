from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SECRET_KEY'] = "secretkey"
application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(application)

@application.before_first_request
def create_tables():
    db.create_all()


from routes import *


if __name__ == '__main__':
    application.run(debug = True)