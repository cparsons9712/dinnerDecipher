from flask import Blueprint, jsonify, session, request, abort
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

    PAYLOAD:
    {"name": STR, "description": STR, "totalTime": STR, "prepTime":STR,"servings": INT,
    "notes": STR, "source": STR, "img_url":STR
    "directions": [{"step": INT, "text": STR},],
    "ingredients": [{"name": STR, "quantity": INT, "unit": STR},]
    }
    """
    # get the directions and ingredients data out of the request so that we can loop and create instances of each
    data = request.json
    directionsArr = data['directions'] if data else None
    ingredientsArr = data['ingredients'] if data else None

    recipe_form = RecipeForm()

    recipe_form['csrf_token'].data = request.cookies['csrf_token']

    if recipe_form.validate_on_submit():
        # Creating the new recipe instance with data from request
        recipe = Recipe()


        recipe_form.populate_obj(recipe)
        recipe.user_id = current_user.id
        db.session.add(recipe)

        #Creating new direction instances for each direction for recipe in payload
        # directions_data = data.get('directions')
        if directionsArr:
        #     # loop through every step in the set of directions
             for step_data in directionsArr:
        #         # send threw flaskForm
                direction_form = DirectionForm(data=step_data)
                direction_form['csrf_token'].data = request.cookies['csrf_token']
                if direction_form.validate():
        #             # in the case of no validation errors, create a new DB instance
                     step = Direction(**step_data, recipe=recipe)
                     db.session.add(step)
                else:
        #             # in case a step of the directions throws a validation error
                    return jsonify({'errors': direction_form.errors}), 400

        # # Create new recipeIngredient instance for each ingredient in payload
        # ingredients_data = data.get('ingredients')
        if ingredientsArr:
        #     # loop through all the ingredients in the ingredients chunk sent in payload
             for ingredient_data in ingredientsArr:
        #         # send each individual ingredient into the flask form for validation
                 ingredient_form = RecipeIngredientForm(data=ingredient_data)
                 ingredient_form['csrf_token'].data = request.cookies['csrf_token']
                 if ingredient_form.validate():
        #             # Make a new database instance if the data set passes validations
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

@recipe_routes.route('/<recipe_id>', methods=['PUT'])
@login_required
def update_recipe(recipe_id):
    """
    Update an existing recipe instance.

    PAYLOAD:
    {"name": STR, "description": STR, "totalTime": STR, "prepTime":STR,"servings": INT,
    "notes": STR, "source": STR, "img_url":STR
    "directions": [{"id": INT, "step": INT, "text": STR},],
    "ingredients": [{"id": INT, "name": STR, "quantity": INT, "unit": STR},]
    }
    """
    # find the db instance of the recipe to update
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404

    # Getting all request data for directions or ingredients
    data = request.json
    directionsArr = data.get('directions', [])
    ingredientsArr = data.get('ingredients', [])

    # initialize a form for the recipe to validate data
    recipe_form = RecipeForm()

    recipe_form['csrf_token'].data = request.cookies['csrf_token']

    # check if the data validated and update the db instance if so
    if recipe_form.validate_on_submit():
        recipe_form.populate_obj(recipe)

        # Update directions
        for direction_data in directionsArr:
            # try to grab the id of the direction
            direction_id = direction_data.get('id')
            if direction_id:
                # if it exist grab the db instance
                direction = Direction.query.get(direction_id)
                if direction:
                    # update the preexisting direction
                    direction.step = direction_data.get('step')
                    direction.text = direction_data.get('text')
                else:
                    #if theres an ID but the direction cant be found throw an error
                    return jsonify({'error': f'Direction with id {direction_id} not found'}), 404
            else:
                #if there is no id (it never existed so we are adding new steps into the recipe) then we need to create a new instance
                direction_form = DirectionForm(data=direction_data)
                direction_form['csrf_token'].data = request.cookies['csrf_token']
                if direction_form.validate():
        #             # in the case of no validation errors, create a new DB instance
                     step = Direction(**direction_data, recipe=recipe)
                     db.session.add(step)
                else:
        #             # in case a step of the directions throws a validation error
                    return jsonify({'errors': direction_form.errors}), 400

        # Update ingredients
        for ingredient_data in ingredientsArr:
            ingredient_id = ingredient_data.get('id')

            # This is a prexisting ingredient we are changing
            if ingredient_id:
                # Get the db instance of the ingredient
                ingredient = RecipeIngredient.query.get(ingredient_id)
                if ingredient:
                    # update the values
                    ingredient.name = ingredient_data.get('name')
                    ingredient.quantity = ingredient_data.get('quantity')
                    ingredient.unit = ingredient_data.get('unit')
                else:
                    # this error for when theres an id, indicating the ingredient exist but we ran into an issue getting the actual database record
                    return jsonify({'error': f'Ingredient with id {ingredient_id} not found'}), 404
            else:
                # If theres no ID then we are adding a new ingredient into the recipe
                 ingredient_form = RecipeIngredientForm(data=ingredient_data)
                 ingredient_form['csrf_token'].data = request.cookies['csrf_token']
                 if ingredient_form.validate():
        #             # Make a new database instance if the data set passes validations
                     ingredient = RecipeIngredient(**ingredient_data, recipe=recipe)
                     db.session.add(ingredient)
                 else:
                     # return the errors to frontend if it doesnt validate
                     return jsonify({'errors': ingredient_form.errors}), 400

        db.session.commit()
        return jsonify({'message': 'Recipe updated successfully'})

    return jsonify({'errors': validation_errors_to_error_messages(recipe_form.errors)}), 400

@recipe_routes.route('/<recipe_id>', methods=['DELETE'])
@login_required
def delete_recipe(recipe_id):
    """
    Removes a recipe from the database
    """
    recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        abort(404, description="Recipe not found")

    db.session.delete(recipe)
    db.session.commit()

    return jsonify({'message': 'Recipe deleted!'})
