from flask import Flask
from flask_sqlalchemy import SQLAlchemy

applications = Flask(__name__)
applications.config['SECRET_KEY'] = "secretkey"
applications.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(applications)

@applications.before_first_request
def create_tables():
    db.create_all()


from routes import *


if __name__ == '__main__':
    applications.run(debug = True)