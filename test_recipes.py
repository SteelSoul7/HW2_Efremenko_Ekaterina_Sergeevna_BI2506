from Part_with_classes import Ingredient
from Part_with_classes import Recipe
from Part_with_classes import ShoppingList
import unittest 

class test_errors(unittest.TestCase):
    def test_error_quantity(self):
        i1 = Ingredient("хлеб", 1000, "г")
        with self.assertRaises(ValueError):
            i1.quantity = 0
        with self.assertRaises(ValueError):
            i1.quantity = -1
    def test_res_error_ratio(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        with self.assertRaises(ValueError):
            self.kotleta.scale(0)
        with self.assertRaises(ValueError):
            self.kotleta.scale(-1)
    def test_valid_portion(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        self.shop = ShoppingList()
        with self.assertRaises(ValueError):
            self.shop.add_recipe(self.kotleta, 0)
        with self.assertRaises(ValueError):
            self.shop.add_recipe(self.kotleta, -1)
            
class TestI:
    def test_creation(self):
        i1 = Ingredient("хлеб", 1000, "г")
        assert i1.name == "хлеб"
        assert i1.quantity == 1000
        assert i1.unit == "г"
    def test_quan(self):
        i1 = Ingredient("хлеб", 1000, "г")
        i1.quantity = 100
        assert i1.quantity == 100

    def test_str(self):
        i1 = Ingredient("хлеб", 1000, "г")
        assert str(i1) == "хлеб: 1000.0 г"
    def test_repr(self):
        i1 = Ingredient("хлеб", 1000, "г")
        assert repr(i1) == 'Ingredient(хлеб, 1000.0, г)'
    def test_eq(self):
        i1 = Ingredient("хлеб", 1000, "г")
        i11 = Ingredient("хлеб", 1000, "г")
        i111 = Ingredient("хлеб", 2000, "г")
        i2 = Ingredient("яйцо", 2, "шт")
        assert i1 == i11
        assert i1 == i111
        assert i1 != i2
        
class TestR:
    def test_creation(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        assert self.kotleta.title == "котлета"
        assert len(self.kotleta.ingredients) == 4
    def test_new(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        self.kotleta.add_ingredient(Ingredient("рис", 50, "г"))
        assert len(self.kotleta.ingredients) == 5
        assert self.kotleta.ingredients[-1].name == "рис"
    def test_add(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        i5 = Ingredient("молоко", 100, "мл")
        self.kotleta.add_ingredient(i5)
        mq = 0
        for i in self.kotleta.ingredients:
            if i.name == "молоко":
                mq = i 
                break
        assert mq.quantity == 400
    def test_valid(self):
        assert Recipe.is_valid_ratio(0) == False
        assert Recipe.is_valid_ratio(-1) == False
        assert Recipe.is_valid_ratio("dfv") == False
        assert Recipe.is_valid_ratio(1) == True
    def test_sc(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        sc = self.kotleta.scale(5)
        assert sc is not self.kotleta
        assert sc.title == self.kotleta.title
        assert sc.ingredients[0].quantity == 5000
        assert self.kotleta.ingredients[0].quantity == 1000
    def test_len(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        assert len(self.kotleta) == 4
        self.kotleta.add_ingredient(Ingredient("молоко", 100, "мл"))
        assert len(self.kotleta.ingredients) == 4 
    def test_str(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.kotleta = Recipe("котлета", [self.i1, self.i2, self.i3, self.i4])
        assert "хлеб" in str(self.kotleta)
        
class TestS:
    def test_add(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.i5 = Ingredient("рис", 50, "г")
        self.kotleta1 = Recipe("котлета1", [self.i1, self.i2, self.i3, self.i4])
        self.kotleta2 = Recipe("котлета2", [self.i2, self.i3, self.i5])
        self.shop = ShoppingList()
        self.shop.add_recipe(self.kotleta1, 1)
        assert len(self.shop._items) == 4
    def test_remove(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.i5 = Ingredient("рис", 50, "г")
        self.kotleta1 = Recipe("котлета1", [self.i1, self.i2, self.i3, self.i4])
        self.kotleta2 = Recipe("котлета2", [self.i2, self.i3, self.i5])
        self.shop = ShoppingList()
        self.shop.add_recipe(self.kotleta1, 1)
        self.shop.add_recipe(self.kotleta2, 1)
        assert len(self.shop._items) == 7
        self.shop.remove_recipe("котлета2")
        assert len(self.shop._items) == 4
        self.shop.remove_recipe("котлета")
        assert len(self.shop._items) == 4
    def test_gl(self):
        self.i1 = Ingredient("хлеб", 1000, "г")
        self.i2 = Ingredient("яйцо", 2, "шт")
        self.i3 = Ingredient("фарш", 2000, "г")
        self.i4 = Ingredient("молоко", 300, "мл")
        self.i5 = Ingredient("рис", 50, "г")
        self.kotleta1 = Recipe("котлета1", [self.i1, self.i2, self.i3, self.i4])
        self.kotleta2 = Recipe("котлета2", [self.i2, self.i3, self.i5])
        self.shop = ShoppingList()
        self.shop.add_recipe(self.kotleta1, 1)
        self.shop.add_recipe(self.kotleta2, 1)
        res = self.shop.get_list()
        mq = 0
        for i in res:
            if i.name == "фарш":
                mq = i.quantity
                break
        assert mq == 4000
        names = [i.name for i in res]
        assert names == sorted(names)
