# fixture_demo.py

import pytest
from ..src import mul as m

@pytest.fixture
def example_fixture():
    return 2

@pytest.fixture
def example_fixture2():
    return 15

def test_with_fixture(example_fixture):
    assert example_fixture == 2

def test_mul(example_fixture, example_fixture2):
    assert m.mulxy(example_fixture, example_fixture2) == 30

def test_add(example_fixture, example_fixture2):
    assert m.addxy(example_fixture, example_fixture2) == 17