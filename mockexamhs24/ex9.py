class Recipe():
    def __init__(self, name, ingdict :dict):
        self.name = name
        self.ingdict = ingdict

    def ingredients_for_servings(self, anz):
        return {key: item * anz for key, item in self.ingdict.items()}

    def __str__(self):
        return f"A recipe for {self.name}"
    
    def __repr__(self):
        return f"Recipe({self.ingdict})"# I need to return [Recipe({'Butter (grams)': 20, 'Garlic, smashed (cloves)': 1, 'Salt (tsp)': 0.25})] probably all the recipies stored in self

class DietRecipe(Recipe):

    def __init__(self, name, ingdict, cal):
        super().__init__(name, ingdict)
        self.cal = cal
    
    def __str__(self):
        return f"A recipe for {self.name} with {self.cal} calories"
    
    def servings_for_calories(self, max_cal):
        return max_cal / self.cal
        

i = {"Butter (grams)": 20, "Garlic, smashed (cloves)": 1, "Salt (tsp)": .25}
recipe = Recipe("Garlic butter", i)
print(recipe.ingredients_for_servings(3))
print(recipe)
print([recipe])
diet_recipe = DietRecipe("Garlic butter", i, 150)
print(diet_recipe.servings_for_calories(300))

# The code above should produce the following output:
"""
{'Butter (grams)': 60, 'Garlic, smashed (cloves)': 3, 'Salt (tsp)': 0.75}
A recipe for Garlic butter
[Recipe({'Butter (grams)': 20, 'Garlic, smashed (cloves)': 1, 'Salt (tsp)': 0.25})]
2.0
"""