from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from flask_login import current_user, login_required
from app.models import Recipe, Direction, RecipeIngredient, db
from app.forms import RecipeForm, RecipeIngredientForm, DirectionForm
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
    # recieve the payload from the request
    data = request.json
    #
    recipe_form = RecipeForm(data=data)
    recipe_form['csrf_token'].data = request.cookies['csrf_token']

    if recipe_form.validate_on_submit():
        # Creating the new recipe instance with data from request
        recipe = Recipe()
        recipe_form.populate_obj(recipe)
        recipe.user_id = current_user.id
        db.session.add(recipe)

        #Creating new direction instances for each direction for recipe in payload
        directions_data = data.get('directions')
        if directions_data:
            # loop through every step in the set of directions
            for step_data in directions_data:
                # send threw flaskForm
                direction_form = DirectionForm(data=directions_data)
                if direction_form.validate():
                    # in the case of no validation errors, create a new DB instance
                    step = Direction(**step_data, recipe=recipe)
                    db.session.add(step)
                else:
                    # in case a step of the directions throws a validation error
                    return jsonify({'errors': direction_form.errors}), 400

        # Create new recipeIngredient instance for each ingredient in payload
        ingredients_data = data.get('ingredients')
        if ingredients_data:
            # loop through all the ingredients in the ingredients chunk sent in payload
            for ingredient_data in ingredients_data:
                # send each individual ingredient into the flask form for validation
                ingredient_form = RecipeIngredientForm(data=ingredient_data)
                if ingredient_form.validate():
                    # Make a new database instance if the data set passes validations
                    ingredient = RecipeIngredient(**ingredient_data, recipe=recipe)
                    db.session.add(ingredient)
                else:
                    # return the errors to frontend if it doesnt validate
                    return jsonify({'errors': ingredient_form.errors}), 400

        # save the changes made to the database and return the new recipe in json formatt
        db.session.commit()
        return recipe.to_dict()
    # if there are errors with the recipe flask form validations return those to the frontend
    return {'errors': validation_errors_to_error_messages(recipe_form.errors)}, 401

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
