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

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

windowsOpended = driver.window_handles

driver.switch_to.window(windowsOpended[1])
message = driver.find_element(By.XPATH, "//div[@class='col-md-8']/p[2]").text
# print(driver.find_element(By.CSS_SELECTOR, ".red").text)

# Split the text as per instruction from Rahul
var = message.split("at")[1].strip().split(" ")[0]  # mentor@rahulshettyacademy.com
driver.switch_to.window(windowsOpended[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(var)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(var)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

# Just grab the message mentor@rahulshettyacademy.com in child window / no need to split
# message = driver.find_element(By.XPATH, "//p[@class='im-para red']/strong").text
# driver.switch_to.window(windowsOpended[0])
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys(message)
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys(message)
# driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)




