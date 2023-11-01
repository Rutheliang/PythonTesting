from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.allegiantair.com/")

if driver.find_element(By.XPATH, "//div[@class='Box-s8oj9r-0 hzaPoz']").is_displayed():
    driver.find_element(By.XPATH, "//img[@alt='closeIcon']").click()

if driver.find_element(By.XPATH, "//div[@class='ot-sdk-container']").is_displayed():
    driver.find_element(By.CSS_SELECTOR, "div[id='onetrust-close-btn-container']").click()

driver.find_element(By.XPATH, "//div[@class='Box-s8oj9r-0 dLFASS']").click()
driver.find_element(By.ID, "firstName").send_keys("Test")
driver.find_element(By.ID, "lastName").send_keys("One")

driver.find_element(By.XPATH, "//div[@data-hook='home-signup_dob-month_dobMonth']").click()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//div[@data-hook='home-signup_dob-month_dobMonth_7']")).click().perform()

driver.find_element(By.XPATH, "//div[@data-hook='home-signup_dob-day_dobDay']").click()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//div[@data-hook='home-signup_dob-day_dobDay_24']")).click().perform()

driver.find_element(By.ID, "dobYear").send_keys("1985")

driver.find_element(By.ID, "email").send_keys("test24@aol.com")
driver.find_element(By.ID, "retypeEmail").send_keys("test24@aol.com")

driver.find_element(By.ID, "password").send_keys("Test@111")
driver.find_element(By.ID, "retypePassword").send_keys("Test@222")

driver.find_element(By.XPATH, "//button[@data-hook='home-signup_submit-button_continue']").click()

error = driver.find_element(By.ID, "retypePassword_error").text
assert "Passwords do not match" == error

#driver.close()