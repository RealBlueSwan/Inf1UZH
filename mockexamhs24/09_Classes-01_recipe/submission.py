class Recipe():
    def __init__(self, name, ingdict :dict):
        self.name = name
        self.ingdict = ingdict

    def ingredients_for_servings(self, anz):
        pass

    def __str__(self):
        pass

class DietRecipe(Recipe):

    def __init__(self, name, ingdict, cal):
        super().__init__(name, ingdict)
        self.cal = cal
    
    def __str__(self):
        return super().__str__()
    
    def servings_for_calories(self):
        pass
    
