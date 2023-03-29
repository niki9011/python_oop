import unittest
from project.mammal import Mammal
class TestMamaml(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Rex", "dog", "bark")

    def test_initialization(self):
        self.assertEqual(self.mammal.name, "Rex")
        self.assertEqual(self.mammal.type, "dog")
        self.assertEqual(self.mammal.sound, "bark")

    def test_make_sound(self):
        self.assertEqual(f"Rex makes bark", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"Rex is of type dog", self.mammal.info())

if __name__ == '__main__':
    unittest.main()
