from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


service_obj = Service() # chrome driver service -> connect automation script to chrome browser
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# chrome driver - intermediate file
# integrating to invoke chrome
# driver is responsible for complete and entire automation on this file
# driver object holds your chrome browser
# service is responsible for the starting and stopping of chrome driver
# you can use the code below (with link) or above code (without link)
#service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64/chromedriver")
#driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()