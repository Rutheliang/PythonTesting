import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver-mac-arm64 2/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.delta.com/")


driver.find_element(By.ID, "fromAirportName").click()

if driver.find_element(By.XPATH, "//button[@class='btn btn-secondary-cta']").is_displayed():
    driver.find_element(By.XPATH, "//button[@class='btn btn-secondary-cta']").click()

if driver.find_element(By.CSS_SELECTOR, ".btn-clear").is_displayed():
    driver.find_element(By.CSS_SELECTOR, ".btn-clear").click()

driver.find_element(By.ID, "search_input").send_keys("LOS")


time.sleep(2)
origins = driver.find_elements(By.XPATH, "//li[@class='airport-list ng-star-inserted']")
for origin in origins:
    origin_state = origin.find_element(By.XPATH, "a/span[2]")
    if origin_state.text == "Los Angeles, CA":
        origin.click()
        break


driver.find_element(By.ID, "toAirportName").click()
driver.find_element(By.ID, "search_input").send_keys("LAS")

time.sleep(2)
destinations = driver.find_elements(By.XPATH, "//li[@class='airport-list ng-star-inserted']")
for destination in destinations:
    destination_state = destination.find_element(By.XPATH, "a/span[2]")
    if destination_state.text == "Las Vegas, NV":
        destination.click()
        break

driver.find_element(By.CSS_SELECTOR, ".calenderDepartSpan").click()

driver.find_element(By.XPATH, "//td[@class='dl-datepicker-available-day'][1]").click()

driver.find_element(By.XPATH, "//tbody[@class='dl-datepicker-tbody-1']/tr[3]/td[1]").click()

driver.find_element(By.CSS_SELECTOR, ".donebutton").click()

driver.find_element(By.ID, "btn-book-submit").click()

time.sleep(2)
classes_departure = driver.find_elements(By.XPATH, "//idp-fare-cell-desktop[@class='fare-cell-item ng-star-inserted']/div")

for class_departure in classes_departure:
    if class_departure.get_attribute("id") == "grid-row-0-fare-cell-desktop-MAIN":
        class_departure.click()
        break

driver.find_element(By.XPATH, "//idp-button[@class='refundable-brand-action-btn']").click()


time.sleep(2)
classes_return = driver.find_elements(By.XPATH, "//idp-fare-cell-desktop[@class='fare-cell-item ng-star-inserted']/div")

for class_return in classes_return:
    if class_return.get_attribute("id") == "grid-row-0-fare-cell-desktop-MAIN":
        class_return.click()
        break

#driver.close()