# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# service_obj = Service("/Users/ruthelia/Downloads/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver - intermediate file

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# chrome
service_obj = Service("/Users/ruthelia/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        # if that box is selected / if it's selected then it's true and no error / if not selection then assertion fail
        break

#radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
#radiobuttons[2].click() # if position will not change then use index
#assert radiobuttons[2].is_selected()

driver.find_element(By.CSS_SELECTOR, "input[value='radio3']").click()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

