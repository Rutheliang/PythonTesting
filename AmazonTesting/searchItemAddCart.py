import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver-mac-arm64 2/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.amazon.com")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("roblox plushies")
time.sleep(2)
#roblox = driver.find_elements(By.XPATH, "//div[@class='s-suggestion-container']")
roblox = driver.find_elements(By.CSS_SELECTOR, "div[class='s-suggestion s-suggestion-ellipsis-direction']")
print(len(roblox))

for robloxP in roblox:
    #if "plush" in robloxP.text:
    if robloxP.text == "roblox plushies for girls":
        robloxP.click()
        break

print(driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value"))

#driver.find_element(By.CSS_SELECTOR, "div[aria-label='roblox plushies']").click()
driver.find_element(By.XPATH, "//li[@aria-label='Roblox']/span/a/div").click()

driver.find_element(By.XPATH, "//li[@aria-label='5 to 7 Years']/span/a/div").click()

driver.find_element(By.XPATH, "//div//div[4]//div//div//div//div//div[2]//div//h2//a//span").click()
#driver.find_element(By.XPATH, "//div[contains(@class,'s-card-container')]/div/div[3]/div[1]/h2/a").click()
#driver.find_element(By.XPATH, "//div[@cel_widget_id='MAIN-SEARCH_RESULTS-1']/div/div/div[3]/div[1]/h2/a").click()
#time.sleep(10)
#products = driver.find_elements(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']")

#for product in products:
#    productName = product.find_element(By.XPATH, "a").text
#    if productName == "Roblox Celebrity Collection - Fashion Icons Four Figure Pack [Includes Exclusive Virtual Item]":
#        product.find_element(By.XPATH, "a/span").click()

driver.find_element(By.CSS_SELECTOR, "input[id='add-to-cart-button']").click()
driver.find_element(By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']").click()
driver.find_element(By.ID, "ap_email").send_keys("test@aol.com")
driver.find_element(By.CSS_SELECTOR, ".a-button-input").click()
driver.find_element(By.ID, "ap_password").send_keys("Test@1234")
driver.find_element(By.ID, "signInSubmit").click()


#driver.close()

