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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
#action.click_and_hold() -> long press
#action.double_click() -> double click
#action.context_click() -> right click
#action.drag_and_drop() -> drag and drop
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# move to and hover / will not perform any actions / always put "perform" for action
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# after hover RIGHT click on Top
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
# move to and hover and click


