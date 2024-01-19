# from app.models import db, Recipe, environment, SCHEMA
# from sqlalchemy.sql import text

# def seed_recipes():
#     one = Recipe(
#         name = "Marshmallow-Surprise Hot Cocoa Cookies",
#         description = "These marshmallow-surprise hot cocoa cookies start with a soft and chewy chocolate cookie made even richer from a helping of hot cocoa mix. Topped with a gooey marshmallow smothered in melted chocolate, they are like a marshmallow-filled hot chocolate bomb, in cookie form!",
#         prepTime = "2hr40Min",
#         totalTime= "3hrs",
#         servings= 20,
#         directions= "In a large bowl using a handheld or stand mixer fitted with a paddle attachment, beat the butter, granulated sugar, and brown sugar together on medium high speed until fluffy and light in color, about 3 minutes. Add the egg and vanilla extract, and then beat on high speed until combined. Scrape down the sides and bottom of the bowl as needed.In a separate bowl, whisk the flour, cocoa powder, hot cocoa mix, baking soda, and salt together until combined. Add the dry ingredients to the bowl with the wet ingredients. Beat on low until combined. The cookie dough will be quite thick. Finally, beat in the milk. The cookie dough will be thick and sticky. Cover dough tightly and chill in the refrigerator for at least 2 hours and up to 3 days. Chilling is imperative for this sticky cookie dough. Preheat oven to 350°F (177°C). Line large baking sheets with parchment paper or silicone baking mats. Set aside. Remove cookie dough from the refrigerator. Scoop and roll dough, a heaping 1 Tablespoon (about 25-26g) each, into balls. Arrange 2 inches apart on the baking sheets.Bake the cookies for just 10 minutes. Remove the cookies from the oven and lightly press a marshmallow half into the tops of each cookie. Return them to the oven and bake for 2 more minutes. Remove from the oven and, using the back of a spoon, gently press down on the marshmallow to slightly flatten it out. Cool cookies on the baking sheet for 10 minutes, and then transfer cookies to a wire rack to cool completeley melt the chocolate: You can melt the chocolate in a double boiler or the microwave. If using the microwave, place the chopped chocolate in a medium heat-proof bowl. Microwave for 20-second increments, stirring after each increment until completely melted and smooth. Spoon melted chocolate over each cooled marshmallow-topped cookie. (When covering with melted chocolate, I usually put the cookies back on a baking sheet, or you can just keep them on the wire rack.) Chocolate sets at room temperature in 30-60 minutes. Once chocolate has set, you can easily store, stack, and transport the cookies. Cover leftover cookies tightly and store at room temperature for up to 1 week.",
#         notes = "Make Ahead & Freezing Instructions: You can make the cookie dough and chill it in the refrigerator for up to 3 days (step 3). Unbaked cookie dough balls freeze well for up to 3 months. Read my tips and tricks on how to freeze cookie dough. Baked and cooled cookies freeze well for up to 3 months. Thaw at room temperature. Keep in mind that after thawing, the chocolate may look streaky on top, or have condensation on the surface. Still fine to eat!",
#         source = "https://sallysbakingaddiction.com/marshmallow-surprise-hot-cocoa-cookies/#tasty-recipes-125132",
#         img_url="https://sallysbakingaddiction.com/wp-content/uploads/2023/11/marshmallow-hot-cocoa-cookies.jpg",
#
#         user_id = 1
#     )
#     two = Recipe(
#         name="Classic Chocolate Chip Cookies",
#         description="The classic chocolate chip cookie, soft and chewy on the inside with a golden-brown exterior. Packed with chocolate chips for the perfect balance of sweetness.",
#         prepTime="15 minutes",
#         totalTime="30 minutes",
#         servings=24,
#         directions="Preheat oven to 350°F (175°C). In a large bowl, cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to the batter along with salt. Stir in flour and chocolate chips. Drop by large spoonfuls onto ungreased pans. Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.",
#         notes="For an extra chewy texture, chill the cookie dough in the refrigerator for at least 24 hours before baking.",
#         source="https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/",
#         img_url="https://handletheheat.com/wp-content/uploads/2019/01/soft-chocolate-chip-cookies-SQUARE.png",
#         ingredients="1 cup (2 sticks) unsalted butter, softened; 3/4 cup granulated sugar; 3/4 cup packed brown sugar; 2 large eggs; 1 teaspoon vanilla extract; 1 teaspoon baking soda; 2 teaspoons hot water; 1/2 teaspoon salt; 3 cups all-purpose flour; 2 cups semisweet chocolate chips",
#         user_id = 1
#     )



#     db.session.add(one)
#     db.session.add(two)


#     db.session.commit()


# def undo_recipes():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM recipes"))

#     db.session.commit()


from app.models import db, Recipe, RecipeIngredient, Direction, environment, SCHEMA
from sqlalchemy.sql import text

def seed_recipes():
    # Seed for Recipe 1: Marshmallow-Surprise Hot Cocoa Cookies
    one = Recipe(
        name="Marshmallow-Surprise Hot Cocoa Cookies",
        description="These marshmallow-surprise hot cocoa cookies start with a soft and chewy chocolate cookie made even richer from a helping of hot cocoa mix. Topped with a gooey marshmallow smothered in melted chocolate, they are like a marshmallow-filled hot chocolate bomb, in cookie form!",
        prepTime="2hr40Min",
        totalTime="3hrs",
        servings=20,
        notes="Make Ahead & Freezing Instructions: You can make the cookie dough and chill it in the refrigerator for up to 3 days (step 3). Unbaked cookie dough balls freeze well for up to 3 months. Read my tips and tricks on how to freeze cookie dough. Baked and cooled cookies freeze well for up to 3 months. Thaw at room temperature. Keep in mind that after thawing, the chocolate may look streaky on top, or have condensation on the surface. Still fine to eat!",
        source="https://sallysbakingaddiction.com/marshmallow-surprise-hot-cocoa-cookies/#tasty-recipes-125132",
        img_url="https://sallysbakingaddiction.com/wp-content/uploads/2023/11/marshmallow-hot-cocoa-cookies.jpg",
        user_id=1
    )

    # Seed ingredients for Recipe 1

    ingredients_one = [
        RecipeIngredient(recipeId=1, name="unsalted butter", quantity=113, unit="g"),
        RecipeIngredient(recipeId=1, name="sugar", quantity=.5, unit="cup"),
        RecipeIngredient(recipeId=1, name="brown sugar", quantity=.5, unit="cup"),
        RecipeIngredient(recipeId=1, name="egg", quantity=1, unit="whole"),
        RecipeIngredient(recipeId=1, name="vanilla extract", quantity=1, unit="teaspoon"),
        RecipeIngredient(recipeId=1, name="flour", quantity=1.5, unit="cup"),
        RecipeIngredient(recipeId=1, name="cocoa powder", quantity=1/3, unit="cup"),
        RecipeIngredient(recipeId=1, name="hot cocoa mix", quantity=1/4, unit="cup"),
        RecipeIngredient(recipeId=1, name="baking soda", quantity=1, unit="teaspoon"),
        RecipeIngredient(recipeId=1, name="salt", quantity=1/8, unit="teaspoon"),
        RecipeIngredient(recipeId=1, name="milk", quantity=2, unit="teaspoons"),
        RecipeIngredient(recipeId=1, name="large marshmellow", quantity=10, unit="whole"),
        RecipeIngredient(recipeId=1, name="semi-sweet chocolate", quantity=8, unit="ounces")
    ]


    # Seed directions for Recipe 1
    directions_one = [
        Direction(recipeId=1, text="In a large bowl using a handheld or stand mixer fitted with a paddle attachment, beat the butter, granulated sugar, and brown sugar together on medium high speed until fluffy and light in color, about 3 minutes."),
        Direction(recipeId=1, text="Add the egg and vanilla extract, and then beat on high speed until combined. Scrape down the sides and bottom of the bowl as needed."),
        Direction(recipeId=1, text="In a separate bowl, whisk the flour, cocoa powder, hot cocoa mix, baking soda, and salt together until combined."),
        Direction(recipeId=1, text="Add the dry ingredients to the bowl with the wet ingredients. Beat on low until combined. The cookie dough will be quite thick."),
        Direction(recipeId=1, text=" Finally, beat in the milk. The cookie dough will be thick and sticky. Cover dough tightly and chill in the refrigerator for at least 2 hours and up to 3 days. Chilling is imperative for this sticky cookie dough."),
        Direction(recipeId=1, text="Preheat oven to 350°F (177°C). Line large baking sheets with parchment paper or silicone baking mats. Set aside."),
        Direction(recipeId=1, text=" Remove cookie dough from the refrigerator. Scoop and roll dough, a heaping 1 Tablespoon (about 25-26g) each, into balls. Arrange 2 inches apart on the baking sheets"),
        Direction(recipeId=1, text="Bake the cookies for just 10 minutes"),
        Direction(recipeId=1, text="Remove the cookies from the oven and lightly press a marshmallow half into the tops of each cookie."),
        Direction(recipeId=1, text="Return them to the oven and bake for 2 more minutes."),
        Direction(recipeId=1, text="Remove from the oven and, using the back of a spoon, gently press down on the marshmallow to slightly flatten it out."),
        Direction(recipeId=1, text="Cool cookies on the baking sheet for 10 minutes, and then transfer cookies to a wire rack to cool completeley"),
        Direction(recipeId=1, text="melt the chocolate: You can melt the chocolate in a double boiler or the microwave. If using the microwave, place the chopped chocolate in a medium heat-proof bowl. Microwave for 20-second increments, stirring after each increment until completely melted and smooth."),
        Direction(recipeId=1, text="Spoon melted chocolate over each cooled marshmallow-topped cookie. (When covering with melted chocolate, I usually put the cookies back on a baking sheet, or you can just keep them on the wire rack.) Chocolate sets at room temperature in 30-60 minutes."),
        Direction(recipeId=1, text=" Once chocolate has set, you can easily store, stack, and transport the cookies. Cover leftover cookies tightly and store at room temperature for up to 1 week"),


    ]

    # Seed for Recipe 2: Classic Chocolate Chip Cookies
    two = Recipe(
        name="Classic Chocolate Chip Cookies",
        description="The classic chocolate chip cookie, soft and chewy on the inside with a golden-brown exterior. Packed with chocolate chips for the perfect balance of sweetness.",
        prepTime="15 minutes",
        totalTime="30 minutes",
        servings=24,
        notes="For an extra chewy texture, chill the cookie dough in the refrigerator for at least 24 hours before baking.",
        source="https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/",
        img_url="https://handletheheat.com/wp-content/uploads/2019/01/soft-chocolate-chip-cookies-SQUARE.png",
        user_id=1
    )

    # Seed ingredients for Recipe 2
    ingredients_two = [
        RecipeIngredient(recipeId=2, name="unsalted butter", quantity=1, unit="cup"),
        RecipeIngredient(recipeId=2, name="granulated sugar", quantity=3/4, unit="cup"),
        RecipeIngredient(recipeId=2, name="brown sugar", quantity=3/4, unit="cup"),
        RecipeIngredient(recipeId=2, name="eggs", quantity=2, unit="whole"),
        RecipeIngredient(recipeId=2, name="vanilla extract", quantity= 1, unit="teaspoon"),
        RecipeIngredient(recipeId=2, name="baking soda", quantity=1, unit="teaspoon"),
        RecipeIngredient(recipeId=2, name="hot water", quantity=2, unit="teaspoons"),
        RecipeIngredient(recipeId=2, name="salt", quantity=1/2, unit="teaspoon"),
        RecipeIngredient(recipeId=2, name="all-purpose flour", quantity=3, unit="cups"),
        RecipeIngredient(recipeId=2, name="semisweet chocolate chips", quantity=2, unit="cups"),
    ]

    # Seed directions for Recipe 2
    directions_two = [
        Direction(recipeId=2, text="Preheat oven to 350°F (175°C)."),
        Direction(recipeId=2, text="In a large bowl, cream together the butter, white sugar, and brown sugar until smooth."),
        Direction(recipeId=2, text="Beat in the eggs one at a time, then stir in the vanilla"),
        Direction(recipeId=2, text="Dissolve baking soda in hot water. Add to the batter along with salt."),
        Direction(recipeId=2, text=" Stir in flour and chocolate chips"),
        Direction(recipeId=2, text="Drop by large spoonfuls onto ungreased pans."),
        Direction(recipeId=2, text="Bake for about 10 minutes in the preheated oven, or until edges are nicely browned."),
        Direction(recipeId=2, text=""),
        Direction(recipeId=2, text=""),
        Direction(recipeId=2, text=""),
        Direction(recipeId=2, text=""),
        Direction(recipeId=2, text=""),
        Direction(recipeId=2, text=""),
        Direction(recipeId=2, text=""),


    ]

    db.session.add(one)
    db.session.add(two)

    for ingredient in ingredients_one + ingredients_two:
        db.session.add(ingredient)

    for direction in directions_one + directions_two:
        db.session.add(direction)

    db.session.commit()

def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipeIngredients RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.directions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipes"))
        db.session.execute(text("DELETE FROM recipeIngredients"))
        db.session.execute(text("DELETE FROM directions"))

    db.session.commit()
