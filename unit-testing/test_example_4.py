import pytest

from example_4 import add


def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(100, 200) == 300
    assert add("sunil", "kumar") == "sunilkumar"