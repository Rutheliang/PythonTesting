from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.amazon.com")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "span[id*='accountList']")).perform()
driver.find_element(By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']").click()
#action.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']")).click().perform()
driver.find_element(By.ID, "ap_customer_name").send_keys("Ruthelia")
driver.find_element(By.ID, "ap_email").send_keys("test@aol.com")
driver.find_element(By.ID, "ap_password").send_keys("Test@1234")
driver.find_element(By.ID, "ap_password_check").send_keys("Test@123")
driver.find_element(By.ID, "continue").click()
passwordMismatch = driver.find_element(By.XPATH, "//div[@id='auth-password-mismatch-alert']/div/div").text

assert "Passwords must match" == passwordMismatch


driver.close()

