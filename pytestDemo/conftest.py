import pytest


@pytest.fixture(scope="class") # scope = class will only run only once not on each method
def setup():
    print("I will be executed first") # open browser
    yield
    print("I will be executed last") # close browser or cookies

#move this to test_fixturesData.py
@pytest.fixture()
def dataLoad():
    print("User Profile Data is being created")
    return ["Ruthel", "Villaespin", "ruthel@yahoo.com"]


#move this to test_demo1_params.py
#@pytest.fixture(params=[("chrome", "Ruthel", "Rodriguez"), ("Firefox", "Villa"), ("IE", "AAA")]) #multiple data
#def crossBrowser(request):
#    return request.param

