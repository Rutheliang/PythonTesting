import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed as strings do not match"
    # if you need to get msg if test fail then add argument
    # text will print if no match


def test_SecondCreditCard():
    a = 2
    b = 6
    assert a+4 == 6, "Addition do not match"






