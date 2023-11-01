from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# chrome
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# different locators selenium provide -> ID, xpath, CSSSelector, ClassName, name, linkText (see Misconceptions_Python file)

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1232332")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath - //tagname[@attribute='value']
# CSS - tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ruthel")

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
# NOTE: value separate by space is another class
# <div class=" alert alert-success alert-dismissible"></div>
# driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message # compare - success is in the message and will pass the test

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain") # 3 text in locators / multiple elements
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

driver.close()


