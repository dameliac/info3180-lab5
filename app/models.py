# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(555), unique=True)
    description = db.Column(db.Text, nullable=True)
    poster = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def serialize(self):
        return{
            "title":self.title,
            "description": self.description,
            "poster": self.poster,
            "created_at": self.created_at
        }
    
    def __repr__(self):
        return "<Movies %r>" % self.title
