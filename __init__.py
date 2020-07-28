from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

db = SQLAlchemy(app)

from views import *

app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SECRET_KEY'] = 'some secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
