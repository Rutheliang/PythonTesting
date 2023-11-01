from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browserSortedVeggies = []
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()

#collect all sorted vegie names -> BrowserSortedVeggie
veggieWebElements = driver.find_elements(By.CSS_SELECTOR, "td:first-child")
# veggieWebEle = driver.find_elements(By.XPATH, "//td[1]")

for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()
# another copy of the list
# you need a copy (put in a variable) before sorting the browserSortedVeggies list

# sort this browserSortedVeggies List -> newSorted List
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList
