import unittest
from python_oop.FINAL_EXAM.project import ToyStore


class TestToyStore(unittest.TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_initialization(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_not_in_dictionary(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("dell", "lenovo")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_name_in_dictionary_raise_exception(self):
        self.store.add_toy("A", "lg")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "lg")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_test_add_toy_not_None(self):
        self.store.add_toy("A", "lg")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Samsung")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_valid(self):
        result = self.store.add_toy("A", "Samsung")

        self.assertEqual("Toy:Samsung placed successfully!", result)
        self.assertEqual("Samsung", self.store.toy_shelf["A"])

    def test_remove_toy_not_dictionary(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("dell", "lenovo")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_non_existing_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Samsung")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_None(self):
        self.store.toy_shelf["A"] = "Samsung"

        result = self.store.remove_toy("A", "Samsung")

        self.assertIsNone(self.store.toy_shelf["A"])
        self.assertEqual("Remove toy:Samsung successfully!", result)


if __name__ == '__main__':
    unittest.main()
