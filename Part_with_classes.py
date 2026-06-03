class Ingredient:
    def __init__ (self, name, quantity, unit):
        self.name = name
        self._quantity = float(quantity)
        self.unit = unit
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, data):
        if data <= 0:
            raise ValueError("Количество должно быть положительным")
        else:
            self._quantity = float(data)
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    def __repr__(self):
        return f"Ingredient({self.name}, {self.quantity}, {self.unit})"
    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit
    
class Recipe:
    def __init__(self, title:str, ingredients: list=[]):
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient):
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio : float) -> bool:
        if isinstance(ratio, (int, float)):
            if ratio > 0:
                return True
            else:
                return False
        return False
    def scale(self, ratio: float):
        if self.is_valid_ratio(ratio) != True:
            raise ValueError("Не вводите мне неверное радио =(")
        new_ingredients = []
        for ing in self.ingredients:
            new_quantity = ing.quantity * ratio
            new_ingredients.append(Ingredient(ing.name, new_quantity, ing.unit))
        return Recipe(self.title, new_ingredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        res = f"Сегодня мы готовим {self.title}! Для этого нам понадобится:\n"
        c = 0
        for ing in self.ingredients:
            c+=1
            res += f"{c}) {ing} \n"
        return res

class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        sc = recipe.scale(portions)
        for i in sc.ingredients:
            self._items.append((i, recipe.title))
    def remove_recipe(self, title: str):
        self._items = [i for i in self._items if i[1] != title]
    def get_list(self):
        result = {}
        for ingredient, tit in self._items:
            if (ingredient.name, ingredient.unit) in result:
                result[(ingredient.name, ingredient.unit)] += ingredient.quantity
            else:
                result[(ingredient.name, ingredient.unit)] = ingredient.quantity
        resres = []
        for (name, unit), quantity in result.items():
            resres.append(Ingredient(name, quantity, unit))
        resres.sort(key=lambda x: x.name)
        return resres 
    def __add__(self, other: 'ShoppingList'):
        merge = ShoppingList()
        merge._items = self._items.copy()
        merge._items.extend(other._items)
        return merge
    
class DietaryRecipe(Recipe):
    def __init__(self, title:str, diet_type: str, ingredients: list=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        if self.is_valid_ratio(ratio) == False:
            raise ValueError("Не вводите мне неверное радио =(")
        sc = super().scale(ratio)
        return DietaryRecipe(sc.title, self.diet_type, sc.ingredients)
    def __str__(self):
        return f"[{self.diet_type}] {self.title}"
