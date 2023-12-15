from .db import db, environment, SCHEMA, add_prefix_for_prod

class Direction(db.Model):
    __tablename__ = 'directions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    recipeId = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
