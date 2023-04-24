from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome driver - intermediate file

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# chrome
service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]//input").send_keys("test@gmail.com") # parent to child xpath
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello1234")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

