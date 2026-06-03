import pytest
from HW_2_OOP_Testing_Git import Ingredient
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