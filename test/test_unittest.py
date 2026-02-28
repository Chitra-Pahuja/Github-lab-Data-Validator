import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import data_validator


class TestDataValidator(unittest.TestCase):

    def test_fun1(self):
        data = [{"name": "Alice", "age": 25}, {"name": None, "age": 30}]
        result = data_validator.fun1(data)
        self.assertEqual(result["name"], 1)
        self.assertEqual(result["age"], 0)

        self.assertEqual(data_validator.fun1([]), {})

        data2 = [{"x": 1}, {"x": 2}, {"x": 3}]
        self.assertEqual(data_validator.fun1(data2), {"x": 0})

    def test_fun2(self):
        data = [{"id": 1}, {"id": 2}, {"id": 2}, {"id": 3}]
        self.assertEqual(data_validator.fun2(data, "id"), [2])

        data2 = [{"id": 1}, {"id": 2}, {"id": 3}]
        self.assertEqual(data_validator.fun2(data2, "id"), [])

        data3 = [{"val": "a"}, {"val": "b"}, {"val": "a"}, {"val": "b"}]
        self.assertEqual(data_validator.fun2(data3, "val"), ["a", "b"])

    def test_fun3(self):
        data = [{"score": 85}, {"score": 90}, {"score": 78}]
        self.assertTrue(data_validator.fun3(data, "score", int))

        data2 = [{"score": 85}, {"score": "ninety"}, {"score": 78}]
        self.assertFalse(data_validator.fun3(data2, "score", int))

        data3 = [{"name": "Alice"}, {"name": "Bob"}]
        self.assertTrue(data_validator.fun3(data3, "name", str))

    def test_fun4(self):
        self.assertEqual(
            data_validator.fun4({"a": 2, "b": 0}, [1, 2], True),
            "Missing: 2 | Duplicates: 2 | TypeCheck: PASS"
        )
        self.assertEqual(
            data_validator.fun4({"x": 0}, [], True),
            "Missing: 0 | Duplicates: 0 | TypeCheck: PASS"
        )
        self.assertEqual(
            data_validator.fun4({"a": 3}, [5], False),
            "Missing: 3 | Duplicates: 1 | TypeCheck: FAIL"
        )
        self.assertEqual(
            data_validator.fun4({}, [], False),
            "Missing: 0 | Duplicates: 0 | TypeCheck: FAIL"
        )


if __name__ == '__main__':
    unittest.main()