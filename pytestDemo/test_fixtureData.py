import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.fixture()
def dataLoad():
    print("User Profile Data is being created")
    return ["Ruthel", "Villaespin", "ruthel@yahoo.com"]


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad): # no need to declare dataload if your not returning data
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])

# in what scenario you will be force to pass fixture name though you declare globally -> need argument if returning a data
# if returning something then mandatory to pass the fixture name into your method