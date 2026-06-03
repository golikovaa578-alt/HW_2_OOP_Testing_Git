import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient_init():
    a = Ingredient("Мука", 500, "г")
    assert a.name == "Мука"
    assert a.quantity == 500.0
    assert a.unit == "г"

def test_ingredient_str():
    a = Ingredient("Мука", 500, "г")
    assert str(a) == "Мука: 500.0 г"

def test_ingredient_eq_same():
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Мука", 200, "г")
    assert a == b

def test_ingredient_eq_different_name():
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Сахар", 500, "г")
    assert a != b

def test_ingredient_eq_different_unit():
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Мука", 500, "кг")
    assert a != b

# 2.2 Тесты Recipe
def test_recipe_init():
    a = Recipe("Пицца")
    assert a.title == "Пицца"
    assert a.ingredients == []

def test_recipe_add_ingredient_new():
    a = Recipe("Пицца")
    a.add_ingredient(Ingredient("Мука", 500, "г"))
    assert len(a.ingredients) == 1

def test_recipe_add_ingredient_duplicate():
    a = Recipe("Пицца")
    a.add_ingredient(Ingredient("Мука", 500, "г"))
    a.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(a.ingredients) == 1
    assert a.ingredients[0].quantity == 700.0

def test_recipe_scale_new_object():
    a = Recipe("Пицца")
    a.add_ingredient(Ingredient("Мука", 500, "г"))
    b = a.scale(2)
    assert b is not a

def test_recipe_scale_quantity():
    a = Recipe("Пицца")
    a.add_ingredient(Ingredient("Мука", 500, "г"))
    b = a.scale(2)
    assert b.ingredients[0].quantity == 1000.0

def test_recipe_scale_invalid():
    a = Recipe("Пицца")
    with pytest.raises(ValueError):
        a.scale(-1)

def test_recipe_len():
    a = Recipe("Пицца")
    a.add_ingredient(Ingredient("Мука", 500, "г"))
    a.add_ingredient(Ingredient("Сахар", 100, "г"))
    assert len(a) == 2

# 2.3 Тесты ShoppingList
def test_shopping_list_add_recipe():
    a = ShoppingList()
    b = Recipe("Пицца")
    b.add_ingredient(Ingredient("Мука", 500, "г"))
    a.add_recipe(b, 2)
    assert len(a._items) == 1

def test_shopping_list_add_recipe_invalid():
    a = ShoppingList()
    b = Recipe("Пицца")
    with pytest.raises(ValueError):
        a.add_recipe(b, 0)

def test_shopping_list_remove_recipe():
    a = ShoppingList()
    b = Recipe("Пицца")
    b.add_ingredient(Ingredient("Мука", 500, "г"))
    a.add_recipe(b, 1)
    a.remove_recipe("Пицца")
    assert len(a._items) == 0

def test_shopping_list_remove_recipe_not_found():
    a = ShoppingList()
    a.remove_recipe("Борщ")

def test_shopping_list_get_list_sum():
    a = ShoppingList()
    b = Recipe("Пицца")
    b.add_ingredient(Ingredient("Мука", 500, "г"))
    c = Recipe("Хлеб")
    c.add_ingredient(Ingredient("Мука", 300, "г"))
    a.add_recipe(b, 1)
    a.add_recipe(c, 1)
    d = a.get_list()
    assert d[0].quantity == 800.0

def test_shopping_list_get_list_sorted():
    a = ShoppingList()
    b = Recipe("Пицца")
    b.add_ingredient(Ingredient("Сахар", 100, "г"))
    b.add_ingredient(Ingredient("Мука", 500, "г"))
    a.add_recipe(b, 1)
    d = a.get_list()
    assert d[0].name == "Мука"
    assert d[1].name == "Сахар"

def test_shopping_list_add():
    a = ShoppingList()
    b = ShoppingList()
    c = Recipe("Пицца")
    c.add_ingredient(Ingredient("Мука", 500, "г"))
    a.add_recipe(c, 1)
    d = a + b
    assert len(d._items) == 1
    assert len(a._items) == 1
    assert len(b._items) == 0