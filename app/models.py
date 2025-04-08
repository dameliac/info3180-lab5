# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(555), unique=True)
    description = db.Column(db.Text, nullable=True)
    poster = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
