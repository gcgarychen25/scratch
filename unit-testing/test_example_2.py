import pytest

from example_2 import devide

def test_validate_age_valid_age():
    assert devide(10,5) == 2

def test_validate_age_invalid_age():
    with pytest.raises(ValueError):
        devide(10,0)