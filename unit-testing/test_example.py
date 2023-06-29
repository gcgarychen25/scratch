from example import add ,concat
import pytest
import unittest

'''def test_add():
    list = [10,20,30,40]
    for i in range(1,len(list)):
        print(f'list i is{list[i]}')
        assert add(list[i], list[i-1]) == list[i]+list[i-1]

def test_concat():
        assert concat("foo", "bar") == "foobar"'''

'''class TestSample:
    def test_add(self):
        assert add(10, 20) == 30

    def test_concat(self):
        assert concat("foo", "bar") == "foobar"'''

'''class TestAddFunction(unittest.TestCase):
    def test_add(self):
        # generating test cases procedurally
        for i in range(-10, 11):
            for j in range(-10, 11):
                with self.subTest(i=i, j=j):
                    self.assertEqual(add(i, j), i + j)'''

'''if __name__ == '__main__':
    unittest.main()'''

'''a = TestAddFunction()
a.test_add()'''

# defining the test function
@pytest.mark.parametrize("a", range(-10, 11))
@pytest.mark.parametrize("b", range(-10, 11))
def test_add(a, b):
    assert add(a, b) == a + b

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

#@timing_decorator # add put this one line before any funciton you wanna test