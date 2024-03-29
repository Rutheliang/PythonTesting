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

service_obj = Service("/Users/ruthelia/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") # ID in the iframe tag
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content() # switch back to default (outside of frame)
print(driver.find_element(By.CSS_SELECTOR, "h3").text)


# How do we know if there's frame in the code -> ask the developer / see "iframe" tag in the code


