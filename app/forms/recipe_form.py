from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from app.models import Recipe


class RecipeForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    description = StringField()
    prepTime = StringField()
    totalTime = StringField()
    servings = IntegerField(validators=[DataRequired(), NumberRange(min=1)])
    directions = TextAreaField(validators=[DataRequired()])
    notes = TextAreaField()
    source = StringField()
    img_url = StringField()
    ingredients = TextAreaField(validators=[DataRequired()])
