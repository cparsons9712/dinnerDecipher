from .db import db, environment, SCHEMA, add_prefix_for_prod

class RecipeIngredient(db.Model):
    __tablename__ = 'recipeIngredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    recipeId = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    # cost = db.Column(db.Integer)
    # ingredientId = db.Column(db.Integer)
