import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass): #inherit from parent to child

    def test_editProfile(self, dataLoad): # need data as returning value / no need to declare dataload if your not returning data
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])
        #print(dataLoad)
        #print(dataLoad[0])
        #print(dataLoad[1])

# in what scenario you will be force to pass fixture name though you declare globally
# if returning something then mandatory to pass the fixture name into your method