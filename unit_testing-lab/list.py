class IntegerList:

    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestsIntegerList(unittest.TestCase):

    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3, 4, 5)

    def test_add_not_type_int_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.int_list.add("cat")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_valid_element(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], self.int_list.add(6))

    def test_remove_index_error_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.int_list.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        self.assertEqual(self.int_list.remove_index(0), 1)
        self.assertEqual([2, 3, 4, 5], self.int_list.get_data())

    def test_get_index_error_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.int_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_index_error_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.int_list.insert(5, 6)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_not_type_int_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.int_list.insert(3, "dog")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_valid_element(self):
        self.int_list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3, 4, 5], self.int_list.get_data())

    def test_get_bigest(self):
        self.assertEqual(self.int_list.get_biggest(), 5)

    def test_get_index(self):
        self.assertEqual(self.int_list.get_index(2), 1)

if __name__ == '__main__':
    unittest.main()
