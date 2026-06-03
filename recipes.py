class Ingredient:
    def __init__(self, a: str, b: float, c: str):
        self.name = a
        self.quantity = b
        self.unit = c
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, b):
        if b <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(b)
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    def __repr__(self):
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

class Recipe:
    def __init__(self, a: str, b: list = None):
        self.title = a
        self.ingredients = b if b is not None else []
    def add_ingredient(self, a):
        for i in self.ingredients:
            if i == a:  # использует __eq__ из Ingredient
                i.quantity += a.quantity
                return
        self.ingredients.append(a)
    @staticmethod
    def is_valid_ratio(a):
        return isinstance(a, (int, float)) and a > 0
    def scale(self, a: float):
        b = Recipe(self.title)
        for i in self.ingredients:
            c = Ingredient(i.name, i.quantity * a, i.unit)
            b.ingredients.append(c)
        return b
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        a = f"Рецепт: {self.title}\nИнгредиенты:\n"
        for i in self.ingredients:
            a += f"  - {i}\n"
        return a

class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, a, b: float):
        if b <= 0:
            raise ValueError("Количество порций должно быть положительным")
        c = a.scale(b)
        for i in c.ingredients:
            self._items.append((i, a.title))
    def remove_recipe(self, a: str):
        self._items = [i for i in self._items if i[1] != a]
    def get_list(self):
        a = {}
        for i in self._items:
            b = i[0]
            c = (b.name, b.unit)
            if c in a:
                a[c] += b.quantity
            else:
                a[c] = b.quantity
        d = [Ingredient(k[0], v, k[1]) for k, v in a.items()]
        return sorted(d, key=lambda x: x.name)
    def __add__(self, a):
        b = ShoppingList()
        b._items = self._items + a._items
        return b

class DietaryRecipe(Recipe):
    def __init__(self, a: str, b: str, c: list = None):
        super().__init__(a, c)
        self.diet_type = b
    def scale(self, a: float):
        b = super().scale(a)
        return DietaryRecipe(self.title, self.diet_type, b.ingredients)
    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"