# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only')])