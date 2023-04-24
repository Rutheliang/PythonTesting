import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver - intermediate file

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# chrome
service_obj = Service("/Users/ruthelia/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

# print(driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value"))

assert (driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value")) == "India"
# compare with expected value


#  Famous question interview - when you update value dynamically thru script
# how do you extract the text? Get attribute of value

