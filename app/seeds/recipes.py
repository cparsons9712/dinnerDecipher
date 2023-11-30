from app.models import db, Recipe, environment, SCHEMA
from sqlalchemy.sql import text

def seed_recipes():
    one = Recipe(
        name = "Marshmallow-Surprise Hot Cocoa Cookies",
        description = "These marshmallow-surprise hot cocoa cookies start with a soft and chewy chocolate cookie made even richer from a helping of hot cocoa mix. Topped with a gooey marshmallow smothered in melted chocolate, they are like a marshmallow-filled hot chocolate bomb, in cookie form!",
        prepTime = "2hr40Min",
        totalTime= "3hrs",
        servings= 20,
        directions= "In a large bowl using a handheld or stand mixer fitted with a paddle attachment, beat the butter, granulated sugar, and brown sugar together on medium high speed until fluffy and light in color, about 3 minutes. Add the egg and vanilla extract, and then beat on high speed until combined. Scrape down the sides and bottom of the bowl as needed.In a separate bowl, whisk the flour, cocoa powder, hot cocoa mix, baking soda, and salt together until combined. Add the dry ingredients to the bowl with the wet ingredients. Beat on low until combined. The cookie dough will be quite thick. Finally, beat in the milk. The cookie dough will be thick and sticky. Cover dough tightly and chill in the refrigerator for at least 2 hours and up to 3 days. Chilling is imperative for this sticky cookie dough. Preheat oven to 350°F (177°C). Line large baking sheets with parchment paper or silicone baking mats. Set aside. Remove cookie dough from the refrigerator. Scoop and roll dough, a heaping 1 Tablespoon (about 25-26g) each, into balls. Arrange 2 inches apart on the baking sheets.Bake the cookies for just 10 minutes. Remove the cookies from the oven and lightly press a marshmallow half into the tops of each cookie. Return them to the oven and bake for 2 more minutes. Remove from the oven and, using the back of a spoon, gently press down on the marshmallow to slightly flatten it out. Cool cookies on the baking sheet for 10 minutes, and then transfer cookies to a wire rack to cool completeley melt the chocolate: You can melt the chocolate in a double boiler or the microwave. If using the microwave, place the chopped chocolate in a medium heat-proof bowl. Microwave for 20-second increments, stirring after each increment until completely melted and smooth. Spoon melted chocolate over each cooled marshmallow-topped cookie. (When covering with melted chocolate, I usually put the cookies back on a baking sheet, or you can just keep them on the wire rack.) Chocolate sets at room temperature in 30-60 minutes. Once chocolate has set, you can easily store, stack, and transport the cookies. Cover leftover cookies tightly and store at room temperature for up to 1 week.",
        notes = "Make Ahead & Freezing Instructions: You can make the cookie dough and chill it in the refrigerator for up to 3 days (step 3). Unbaked cookie dough balls freeze well for up to 3 months. Read my tips and tricks on how to freeze cookie dough. Baked and cooled cookies freeze well for up to 3 months. Thaw at room temperature. Keep in mind that after thawing, the chocolate may look streaky on top, or have condensation on the surface. Still fine to eat!",
        source = "https://sallysbakingaddiction.com/marshmallow-surprise-hot-cocoa-cookies/#tasty-recipes-125132",
        img_url="https://sallysbakingaddiction.com/wp-content/uploads/2023/11/marshmallow-hot-cocoa-cookies.jpg",
        ingredients = "1/2 cup (8 Tbsp; 113g) unsalted butter, softened to room temperature ; 1/2 cup (100g) granulated sugar; 1/2 cup (100g) packed light or dark brown sugar; 1 large egg, at room temperature; 1 teaspoon pure vanilla extract; 1 and 1/2 cups (188g) all-purpose flour (spooned & leveled); 1/3 cup (27g) natural unsweetened cocoa powder; 1/4 cup (40g) dry hot cocoa mix; 1 teaspoon baking soda; 1/8 teaspoon salt; 2 teaspoons (10ml) milk (any kind, dairy or nondairy, is fine); Topping; 10 large marshmallows, cut in half; 8 ounces (226g) semi-sweet chocolate, finely chopped (see Note)",
        user_id = 1
    )
    two = Recipe(
        name="Classic Chocolate Chip Cookies",
        description="The classic chocolate chip cookie, soft and chewy on the inside with a golden-brown exterior. Packed with chocolate chips for the perfect balance of sweetness.",
        prepTime="15 minutes",
        totalTime="30 minutes",
        servings=24,
        directions="Preheat oven to 350°F (175°C). In a large bowl, cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to the batter along with salt. Stir in flour and chocolate chips. Drop by large spoonfuls onto ungreased pans. Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.",
        notes="For an extra chewy texture, chill the cookie dough in the refrigerator for at least 24 hours before baking.",
        source="https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/",
        img_url="https://www.example.com/chocolate-chip-cookies.jpg",
        ingredients="1 cup (2 sticks) unsalted butter, softened; 3/4 cup granulated sugar; 3/4 cup packed brown sugar; 2 large eggs; 1 teaspoon vanilla extract; 1 teaspoon baking soda; 2 teaspoons hot water; 1/2 teaspoon salt; 3 cups all-purpose flour; 2 cups semisweet chocolate chips"
    )

    three = Recipe(
        name="Vegetarian Spaghetti Bolognese",
        description="A hearty and flavorful vegetarian version of the classic spaghetti Bolognese. Made with plant-based protein, tomatoes, and a blend of Italian herbs for a satisfying meal.",
        prepTime="20 minutes",
        totalTime="40 minutes",
        servings=6,
        directions="Cook spaghetti according to package instructions. In a large skillet, heat olive oil over medium heat. Add onion, garlic, and plant-based protein. Cook until onions are soft and protein is browned. Stir in crushed tomatoes, tomato paste, vegetable broth, Italian seasoning, salt, and pepper. Simmer for 15-20 minutes. Serve the sauce over cooked spaghetti. Garnish with fresh basil and grated Parmesan.",
        notes="For a vegan option, use plant-based Parmesan or nutritional yeast instead of traditional Parmesan cheese.",
        source="https://www.example.com/vegetarian-spaghetti-bolognese/",
        img_url="https://www.example.com/vegetarian-bolognese.jpg",
        ingredients="16 oz spaghetti; 2 tbsp olive oil; 1 onion, finely chopped; 3 cloves garlic, minced; 1 lb plant-based protein (e.g., soy crumbles or lentils); 28 oz crushed tomatoes; 2 tbsp tomato paste; 1 cup vegetable broth; 2 tsp Italian seasoning; Salt and pepper to taste; Fresh basil and Parmesan cheese for garnish"
    )

    four = Recipe(
        name="Mango Avocado Salsa",
        description="A refreshing and colorful mango avocado salsa, perfect for serving with tortilla chips or as a topping for grilled fish or chicken. The combination of sweet mango and creamy avocado is simply irresistible.",
        prepTime="15 minutes",
        totalTime="15 minutes",
        servings=4,
        directions="In a bowl, combine diced mango, diced avocado, red onion, cilantro, and jalapeño. Drizzle with lime juice and gently toss to combine. Season with salt and pepper to taste. Refrigerate for at least 30 minutes before serving to allow the flavors to meld. Serve with tortilla chips or as a topping for grilled dishes.",
        notes="Adjust the level of spiciness by adding more or less jalapeño, depending on your preference.",
        source="https://www.example.com/mango-avocado-salsa/",
        img_url="https://www.example.com/mango-avocado-salsa.jpg",
        ingredients="1 ripe mango, diced; 1 ripe avocado, diced; 1/4 cup red onion, finely chopped; 2 tbsp fresh cilantro, chopped; 1 jalapeño, seeds removed and finely chopped; Juice of 1 lime; Salt and pepper to taste"
    )

    five = Recipe(
        name="Quinoa Salad with Roasted Vegetables",
        description="A nutritious and colorful quinoa salad with a medley of roasted vegetables. Packed with protein and fiber, this salad is perfect for a healthy and satisfying meal.",
        prepTime="20 minutes",
        totalTime="40 minutes",
        servings=4,
        directions="Preheat oven to 400°F (200°C). Toss diced vegetables (bell peppers, cherry tomatoes, zucchini, and red onion) with olive oil, salt, and pepper. Spread on a baking sheet and roast for 25-30 minutes until vegetables are tender. In a separate pot, cook quinoa according to package instructions. Allow quinoa and roasted vegetables to cool. In a large bowl, combine quinoa, roasted vegetables, chickpeas, and feta cheese. Drizzle with balsamic vinaigrette and toss to combine. Serve chilled.",
        notes="Feel free to customize the vegetables based on your preferences. Add a protein of your choice for an extra boost.",
        source="https://www.example.com/quinoa-roasted-vegetable-salad/",
        img_url="https://www.example.com/quinoa-salad.jpg",
        ingredients="1 cup quinoa; 2 cups diced mixed vegetables (bell peppers, cherry tomatoes, zucchini, red onion); 2 tbsp olive oil; Salt and pepper to taste; 1 can chickpeas, drained and rinsed; 1/2 cup feta cheese, crumbled; Balsamic vinaigrette for dressing"
    )

    six = Recipe(
        name="Grilled Lemon Herb Chicken",
        description="Juicy and flavorful grilled lemon herb chicken, marinated in a blend of herbs and citrus for a delicious and easy-to-make main course. Perfect for summer barbecues or a quick weeknight dinner.",
        prepTime="15 minutes",
        totalTime="30 minutes",
        servings=4,
        directions="In a bowl, whisk together olive oil, lemon juice, garlic, rosemary, thyme, salt, and pepper to create the marinade. Place chicken breasts in a resealable plastic bag and pour the marinade over them. Seal the bag and refrigerate for at least 2 hours, or overnight for best flavor. Preheat grill to medium-high heat. Remove chicken from the marinade and grill for 6-7 minutes per side, or until the internal temperature reaches 165°F (74°C). Let the chicken rest for a few minutes before serving.",
        notes="Try marinating the chicken in advance for more intense flavor. Serve with your favorite side dishes or sliced over a salad.",
        source="https://www.example.com/grilled-lemon-herb-chicken/",
        img_url="https://www.example.com/grilled-chicken.jpg",
        ingredients="4 boneless, skinless chicken breasts; 1/4 cup olive oil; Juice of 2 lemons; 3 cloves garlic, minced; 1 tsp dried rosemary; 1 tsp dried thyme; Salt and pepper to taste"
    )

    db.session.add(one, two, three, four, five, six)
    db.session.commit()


def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipes"))

    db.session.commit()
