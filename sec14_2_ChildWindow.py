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

service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsOpened = driver.window_handles
# window handles grab the list of windows / parent window is index 0

driver.switch_to.window(windowsOpened[1])
# open second window / child window
print(driver.find_element(By.TAG_NAME,"h3").text)
# driver.close() # Child be will closed and go back to parent window

driver.switch_to.window(windowsOpened[0])
# go back to first window / parent window

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

