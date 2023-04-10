from python_oop.FINAL_EXAM.project import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):

    def setUp(self) -> None:
        self.shopping = ShoppingCart("Lidl", 6.6)

    def test__init__(self):
        self.assertEquals(self.shopping.shop_name, "Lidl")
        self.assertEquals(self.shopping.budget, 6.6)
        self.assertEquals(self.shopping.products, {})

    def test_name_not_upper(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping.shop_name = "shop"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_not_isalpha(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping.shop_name = "546"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_price_over_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping.add_to_cart("Shirt", 100.00)
        self.assertEquals(str(ve.exception), f"Product Shirt cost too much!")

    def test_add_to_cart_valid(self):
        self.assertEquals(self.shopping.add_to_cart("Shirt", 99.99), f"Shirt product was successfully added to the cart!")
        self.assertEquals(self.shopping.products, {"Shirt": 99.99})

    def test_remove_from_cart(self):
        self.shopping.add_to_cart("Jacket", 99.99)
        self.shopping.add_to_cart("Shirt", 99.99)
        self.assertEquals(self.shopping.remove_from_cart("Jacket"),
                          f"Product Jacket was successfully removed from the cart!")
        self.assertEquals(self.shopping.products, {"Shirt": 99.99})

    def test_remove_from_cart_not_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping.remove_from_cart("Glasses")
        self.assertEqual(str(ve.exception), "No product with name Glasses in the cart!")

    def test__add__

if __name__ == '__main__':
    unittest.main()