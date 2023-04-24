from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browserSortedVeggies = []
service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()

#collect all sorted vegie names -> BrowserSortedVeggie
veggieWebEle = driver.find_elements(By.CSS_SELECTOR, "td:first-child")
# veggieWebEle = driver.find_elements(By.XPATH, "//td[1]")

for ele in veggieWebEle:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy() # another copy of the list

# sort this browserSortedVeggies List -> newSorted List
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList
