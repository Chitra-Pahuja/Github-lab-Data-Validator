import pytest
from src import data_validator


def test_fun1():
    data = [{"name": "Alice", "age": 25}, {"name": None, "age": 30}]
    result = data_validator.fun1(data)
    assert result["name"] == 1
    assert result["age"] == 0

    assert data_validator.fun1([]) == {}

    data2 = [{"x": 1}, {"x": 2}, {"x": 3}]
    assert data_validator.fun1(data2) == {"x": 0}

    data3 = [{"a": None}, {"a": None}]
    assert data_validator.fun1(data3) == {"a": 2}


def test_fun2():
    data = [{"id": 1}, {"id": 2}, {"id": 2}, {"id": 3}]
    assert data_validator.fun2(data, "id") == [2]

    data2 = [{"id": 1}, {"id": 2}, {"id": 3}]
    assert data_validator.fun2(data2, "id") == []

    data3 = [{"val": "a"}, {"val": "b"}, {"val": "a"}, {"val": "b"}]
    assert data_validator.fun2(data3, "val") == ["a", "b"]

    data4 = [{"id": 5}, {"id": 5}, {"id": 5}]
    assert data_validator.fun2(data4, "id") == [5]


def test_fun3():
    data = [{"score": 85}, {"score": 90}, {"score": 78}]
    assert data_validator.fun3(data, "score", int) == True

    data2 = [{"score": 85}, {"score": "ninety"}, {"score": 78}]
    assert data_validator.fun3(data2, "score", int) == False

    data3 = [{"name": "Alice"}, {"name": "Bob"}]
    assert data_validator.fun3(data3, "name", str) == True

    data4 = [{"price": 9.99}, {"price": 4.50}]
    assert data_validator.fun3(data4, "price", float) == True


def test_fun4():
    assert data_validator.fun4({"a": 2, "b": 0}, [1, 2], True) == "Missing: 2 | Duplicates: 2 | TypeCheck: PASS"
    assert data_validator.fun4({"x": 0}, [], True) == "Missing: 0 | Duplicates: 0 | TypeCheck: PASS"
    assert data_validator.fun4({"a": 3}, [5], False) == "Missing: 3 | Duplicates: 1 | TypeCheck: FAIL"

    assert data_validator.fun4({}, [], False) == "Missing: 0 | Duplicates: 0 | TypeCheck: FAIL"