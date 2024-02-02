from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from app.models import Direction


class DirectionForm(FlaskForm):
    step = IntegerField()
    text = StringField()

