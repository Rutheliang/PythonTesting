import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument("headless")

service_obj = Service("/Users/ruthelia/Downloads/chromedriver-mac-arm64 2/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.amazon.com")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("roblox")
time.sleep(2)

roblox = driver.find_elements(By.XPATH, "//div[@class='s-suggestion-container']")
print(len(roblox))

for item in roblox:
    itemName = item.find_element(By.XPATH, "div")
    if itemName.text == "roblox toys":
        itemName.click()
        break

driver.find_element(By.XPATH, "//li[@id='p_36/1253560011']").click()
driver.find_element(By.XPATH, "//li[@aria-label='5 to 7 Years']/span/a/div").click()
driver.find_element(By.XPATH, "//li[@aria-label='Plastic']").click()

driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result'][2]").click()
driver.find_element(By.CSS_SELECTOR, "input[id='add-to-cart-button']").click()
driver.find_element(By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']").click()
driver.find_element(By.ID, "ap_email").send_keys("test@aol.com")
driver.find_element(By.CSS_SELECTOR, ".a-button-input").click()
driver.find_element(By.ID, "ap_password").send_keys("Test@1234")
driver.find_element(By.ID, "signInSubmit").click()


driver.close()

