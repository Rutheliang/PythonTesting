import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

expectList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# wait for 2 seconds to load
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    # actualList.append(result.find_element(By.CSS_SELECTOR, "div[class='product'] h4").text)
    actualList.append(result.find_element(By.XPATH, "h4").text)
    #chaining meaning h4 is equal to //div[@class='products']/div/h4
    result.find_element(By.XPATH, "div/button").click()

assert expectList == actualList

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)


totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)


discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
#float is decimal values

assert totalAmount > discountAmount