from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from flask_login import current_user, login_required
from app.models import Recipe, db
from app.forms import RecipeForm
from .auth_routes import validation_errors_to_error_messages

recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('/')
# @login_required
def all_recipes():
    """
    Query for all recipes in the database
    """
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route('/', methods=['POST'])
@login_required
def create_recipe():
    """
    Create a new database instance of a recipe.
    """
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        recipe = Recipe()
        form.populate_obj(recipe)
        recipe.user_id = current_user.id
        db.session.add(recipe)
        db.session.commit()
        return recipe.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@recipe_routes.route('<recipe_id>', methods=['PUT'])
@login_required
def update_recipe(recipe_id):
    """
    Updates an instance of a recipe in the database
    """
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    recipe = Recipe.query.get_or_404(recipe_id)

    if form.validate_on_submit():

        form.populate_obj(recipe)
        recipe.user_id = current_user.id
        db.session.add(recipe)
        db.session.commit()
        return recipe.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@recipe_routes.route('<recipe_id>', methods=['DELETE'])
@login_required
def delete_recipe(recipe_id):
    """
    Removes a recipe from the database
    """
    recipe = Recipe.query.filter(Recipe.id == recipe_id).first()
    if recipe is None:
        return {'errors': {'Not Found': 'A task with this id could not be located'}}, 404
    db.session.delete(recipe)
    db.session.commit()

    return {'message': 'Recipe deleted!'}
