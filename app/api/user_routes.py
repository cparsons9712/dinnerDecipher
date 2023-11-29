from flask import Blueprint, jsonify
from flask_login import login_required,current_user
from app.models import User, Recipe

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/recipes')
@login_required
def users_recipes():
    """
    Query for all recipes in the database created by the user
    """
    recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}
