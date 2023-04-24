from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

name = "Ruthel"

# chrome
service_obj = Service("/Users/ruthelia/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='enter-name']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
# switch browser to alert mode
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

assert name in alertText

alert.accept() # to click ok (positive)
#  alert.dismiss() # -> to dismiss or cancel (negative)


