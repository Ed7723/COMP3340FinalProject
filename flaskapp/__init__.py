from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Config for security. Secret key is used for secure signin for session cookies.
app.config['SECRET_KEY'] = '23d7a1eda8fff64969fac5ebce9d7d92'
# Specifies the location of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Create SQL Alchemy database instance
db = SQLAlchemy(app)

from flaskapp import routes

