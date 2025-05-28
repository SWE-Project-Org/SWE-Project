class Ingredients:
    def __init__(self, ingredients: list[tuple[str, int]]):
        self.ingredients = ingredients
       

    def to_tuple(self):
        return self.ingredients