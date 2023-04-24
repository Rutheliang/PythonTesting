import pytest


#@pytest.fixture() -> declare in conftest.py
#def setup():
#    print("I will be executed first")  # open browser
#    yield
 #   print("I will be executed last")  # close browser or cookies


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
