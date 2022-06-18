
class Receta:
    def __init__(self, title, id, servings, cooking_time, ingredients):
        self.title = title
        self.id = id
        self.servings = servings
        self.cooking_time = cooking_time
        self.ingredients = ingredients

    def __str__(self):
        return f'\n\t~ {self.title} ~' \
               f'\n\tId: {self.id}' \
               f'\n\tServings: {self.servings}' \
               f'\n\tCooking time: {self.cooking_time}' \
               f'\n\tIngredients: {self.ingredients}'

    def serialize(self):
        return {
            'Title': self.title,
            'ID': self.id,
            'Servings': self.servings,
            'Cooking time': self.cooking_time,
            'Ingredients' : self.ingredients
        }