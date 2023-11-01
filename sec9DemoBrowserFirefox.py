from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# chrome driver - intermediate file

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# firefox
service_obj = Service("/Users/ruthelia/Downloads/geckodriver 2")
driver = webdriver.Firefox(service=service_obj)

# microsoft edge
# search microsoft edge webdriver
#service_obj = Service("/Users/ruthelia/Downloads/msedgedriver")
#driver = webdriver.Firefox(service=service_obj)


driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()