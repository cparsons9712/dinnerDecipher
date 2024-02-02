from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from app.models import RecipeIngredient


class RecipeIngredientForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    quantity = IntegerField()
    unit = StringField()
