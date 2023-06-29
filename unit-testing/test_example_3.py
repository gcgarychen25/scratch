import sys
import pytest

from example_3 import add

@pytest.mark.skip(reason="just skip it")
def test_add_1():
    assert add(10, 20) == 30

@pytest.mark.skipif(sys.version_info < (3, 11), reason="requires python3.11 or higher")
def test_add_2():
    assert add(20, 20) == 50

@pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
def test_add_3():
    assert add(20, 20) == 40

@pytest.mark.xfail(sys.platform == "darwin", reason="fail the test if run on darwin")
def test_add_4():
    assert add(20, 20) == 50

@pytest.mark.xfail(reason="known parser issue")
def test_add_5():
    assert add(20, 20) == 40
@pytest.mark.xfail(reason="known parser issue")
def test_add_4():
    assert add(20, 20) == 40