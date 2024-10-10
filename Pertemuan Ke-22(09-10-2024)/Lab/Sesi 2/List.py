class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for arg in args:
            if isinstance(arg, int):
                self.__data.append(arg)
            else:
                raise ValueError("Only integers are allowed")

    def add(self, element):
        if not isinstance(element, int):
            raise ValueError("Only integers are allowed")
        self.__data.append(element)
        return self.__data

    def remove_index(self, index):
        if index < 0 or index >= len(self.__data):
            raise IndexError("Index is out of range")
        return self.__data.pop(index)

    def get(self, index):
        if index < 0 or index >= len(self.__data):
            raise IndexError("Index is out of range")
        return self.__data[index]

    def insert(self, index, element):
        if not isinstance(element, int):
            raise ValueError("Only integers are allowed")
        if index < 0 or index >= len(self.__data):
            raise IndexError("Index is out of range")
        self.__data.insert(index, element)

    def get_biggest(self):
        return max(self.__data)

    def get_index(self, element):
        return self.__data.index(element)

import unittest

class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2, 3)

    def test_constructor_stores_only_integers(self):
        self.assertEqual(self.int_list._IntegerList__data, [1, 2, 3])
        with self.assertRaises(ValueError):
            IntegerList(1, 'a', 3.5)

    def test_add_adds_integer_and_returns_list(self):
        result = self.int_list.add(4)
        self.assertEqual(result, [1, 2, 3, 4])
        with self.assertRaises(ValueError):
            self.int_list.add('not an integer')

    def test_remove_index_removes_element_at_index_and_returns_it(self):
        result = self.int_list.remove_index(1)
        self.assertEqual(result, 2)
        self.assertEqual(self.int_list._IntegerList__data, [1, 3])
        with self.assertRaises(IndexError):
            self.int_list.remove_index(5)

    def test_get_returns_element_at_index(self):
        self.assertEqual(self.int_list.get(1), 2)
        with self.assertRaises(IndexError):
            self.int_list.get(5)

    def test_insert_adds_element_at_index(self):
        self.int_list.insert(1, 5)
        self.assertEqual(self.int_list._IntegerList__data, [1, 5, 2, 3])
        with self.assertRaises(IndexError):
            self.int_list.insert(10, 5)
        with self.assertRaises(ValueError):
            self.int_list.insert(1, 'not an integer')

    def test_get_biggest_returns_biggest_integer(self):
        self.assertEqual(self.int_list.get_biggest(), 3)

    def test_get_index_returns_index_of_element(self):
        self.assertEqual(self.int_list.get_index(3), 2)
        with self.assertRaises(ValueError):
            self.int_list.get_index(10)


if __name__ == '__main__':
    unittest.main()
