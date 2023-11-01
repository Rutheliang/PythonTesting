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
#chrome_options.add_argument("headless") # NOT OPEN BROWSER
chrome_options.add_argument("--ignore-certificate-errors") # IGNORE CERTIFICATE

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") # Go to button
driver.execute_script("window.scrollTo(0,10);") # Go to Top
#driver.execute_script("window.scrollBy(0,700);") # specific height
# SCROLL DOWN USING JAVA SCRIPT
# Click on inspect, go to Console, type "window.scrollBy(0, 700)"
# Use scroll if window sometimes element is not visible in view. Somewhere in button requires scrolling.

driver.get_screenshot_as_file("screen.png") # simple screenshot


