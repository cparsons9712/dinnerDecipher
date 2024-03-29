from .db import db, environment, SCHEMA, add_prefix_for_prod

class Recipe(db.Model):
    __tablename__ = 'recipes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    description = db.Column(db.String(255))
    prepTime = db.Column(db.String(10))
    totalTime = db.Column(db.String(10))
    servings = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.Text)
    source = db.Column(db.String(150))
    img_url = db.Column(db.String(255))
    # ingredients = db.Column(db.Text, nullable=False)

    #Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    directions = db.relationship('Direction', backref='recipe', lazy=True, cascade="all, delete-orphan")
    ingredients = db.relationship('RecipeIngredient', backref = 'recipe', lazy=True, cascade="all, delete-orphan")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'prepTime': self.prepTime,
            'totalTime': self.totalTime,
            'servings': self.servings,
            'notes': self.notes,
            'source': self.source,
            'img_url': self.img_url,
            'ingredients': [ingredient.to_dict() for ingredient in self.ingredients],
            'directions': [direction.to_dict() for direction in self.directions]
        }
