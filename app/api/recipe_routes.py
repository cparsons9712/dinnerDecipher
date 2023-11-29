from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Recipe

recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('/')
@login_required
def all_recipes():
    """
    Query for all recipes in the database
    """
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}


