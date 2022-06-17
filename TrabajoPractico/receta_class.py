
class Receta:
    def __init__(self, title, id):
        self.title = title
        self.id = id

    def __str__(self):
        return f'\n\t~ {self.title} ~' \
               f'\n\tId: {self.id}'