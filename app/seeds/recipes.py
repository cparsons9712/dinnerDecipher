from app.models import db, Recipe, environment, SCHEMA
from sqlalchemy.sql import text
from faker import Faker
import random

fake = Faker()

# Assuming you have a User model defined
# from app.models import User

# Create 10 seed recipes
for _ in range(10):
    # For simplicity, I'm assuming you have at least one user in the database.
    # You might need to adjust this depending on your actual User model and database setup.
    user_id = random.randint(1, 10)  # Assuming user IDs go up to 10

    recipe = Recipe(
        name=fake.words(3),
        description=fake.sentence(),
        prepTime=fake.time(),
        totalTime=fake.time(),
        servings=random.randint(1, 6),  # Assuming servings are between 1 and 6
        directions=fake.paragraph(),
        notes=fake.text(),
        source=fake.company(),
        img_url=fake.image_url(),
        ingredients=fake.text(),
        user_id=user_id
    )

    db.session.add(recipe)

# Commit the changes
db.session.commit()
