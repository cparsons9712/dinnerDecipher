from .db import db, environment, SCHEMA, add_prefix_for_prod

class RecipeIngredient(db.Model):
    __tablename__ = 'recipeIngredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    recipeId = db.Column(db.Integer)
    ingredientId = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    unit = db.Column(db.String)
    cost = db.Column(db.Integer)
