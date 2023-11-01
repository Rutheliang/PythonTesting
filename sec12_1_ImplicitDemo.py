import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver-mac-arm64 2/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# IMPLICIT
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# wait for 2 seconds to load

time.sleep(2)
#web elements list is special/ it will get caught on implicit wait / exceptional case so always use time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(results)
print(count)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()
    # chaining from parent to child
    # //div[class='product'/div/button] / parent -> div[class='product'] / child -> div/button
    # there's 1 button only in div so no need to use div[3]

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(5) -> not need since we have implicit
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

