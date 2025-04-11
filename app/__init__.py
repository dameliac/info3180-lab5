from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
UPLOAD_FOLDER='./app/uploads'
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'Som3$ec5etK*y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysql@localhost/lab5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#exercise 4
csrf= CSRFProtect(app)
#exercise 3
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models