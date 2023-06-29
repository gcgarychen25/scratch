import pytest

from example_4 import add

@pytest.mark.parametrize("num1,num2,expected", [(1,2,3), (2,3,5), (100,200,300),("sunil","kumar","sunilkumar")])
def test_eval(num1,num2, expected):
    assert add(num1,num2) == expected