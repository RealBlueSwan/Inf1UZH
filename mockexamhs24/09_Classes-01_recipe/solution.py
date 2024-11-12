#!/usr/bin/env python3

class Recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def ingredients_for_servings(self, n):
        return {name: amount * n for name, amount in self.ingredients.items()}

    def __str__(self):
        return f"A recipe for {self.name}"

    def __repr__(self):
        return f"Recipe({repr(self.ingredients)})"

class DietRecipe(Recipe):
    def __init__(self, name, ingredients, calories):
        super().__init__(name, ingredients)
        self.calories = calories

    def servings_for_calories(self, n):
        return n / self.calories


# examples
i = {"Butter (grams)": 20, "Garlic, smashed (cloves)": 1, "Salt (tsp)": .25}
recipe = Recipe("Garlic butter", i)
print(recipe.ingredients_for_servings(3))
print(recipe)
print([recipe])
diet_recipe = DietRecipe("Garlic butter", i, 150)
print(diet_recipe.servings_for_calories(300))
