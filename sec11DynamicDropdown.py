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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a") # CSS -> li[class='ui-menu-item'] a"
# print(len(cntry)) -> #count the number of items in list variables

for country in countries:
    if country.text == "India":
        country.click()
        break  # exit the loop / stop and will not find the other country

#if you want to get the value and print, use "get.attribute" and not ".text"
#value "india" is handle thru script dynamically so use get.attribute
# print(driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value"))

assert (driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value")) == "India"
# compare with expected value


#  Famous question interview - when you update value dynamically thru script
# how do you extract the text? Get attribute of value

