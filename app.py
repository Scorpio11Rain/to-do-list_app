from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()


from routes import *


if __name__ == '__main__':
    app.run(debug = True)