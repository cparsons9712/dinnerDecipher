from .db import db, environment, SCHEMA, add_prefix_for_prod

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    servingSizeinG = db.Column(db.Integer, nullable=False)
    kcal = db.Column(db.Integer)
    carb = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    protien = db.Column(db.Integer)
    satFat = db.Column(db.Integer)
    transFat = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    fiber = db.Column(db.Integer)
    sugar = db.Column(db.Integer)
    cost = db.Column(db.Integer)
