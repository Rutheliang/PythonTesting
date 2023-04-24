# any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped  in method only
# every method is a test case
# method name should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) test @pytest.mark.smoke and then run with -m
# you can skip test with @pytest.mark.skip
# skip particular test not method / no result -> @pytest.mark.xfail
# fixtures are used to set up and tear down methods for test cases -> conftest file to generalize fixture
# (continuation) make it available to all test cases (fixture name into parameter of method)
# data driven and parameterization can be done with return statements in tuple (list with this symbol []) format
# when you define fixture scope to class only, it will run once before class is initiated and at the end


import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Ruthel")


@pytest.mark.xfail
def test_secondCreditCard():
    print("Good morning")


@pytest.fixture(params=[("chrome", "Ruthel", "Rodriguez"), ("Firefox", "Villa"), ("IE", "AAA")])  # multiple data
def crossBrowser(request):
    return request.param


def test_crossBrowser(crossBrowser):  # parameterize with multiple values
    print(crossBrowser[1])
