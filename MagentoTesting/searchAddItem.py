import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.ID, "ui-id-4")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//a[@id='ui-id-9']/span[2]")).click().perform()

driver.find_element(By.XPATH, "//div[@id='narrow-by-list']/div[1]").click()
#driver.find_element(By.XPATH, "//div[@id='narrow-by-list']/div[1]/div[2]").click()

time.sleep(2)

tops = driver.find_elements(By.XPATH, "//strong[@class='product name product-item-name']/a")

for item in tops:
    if item.text == "Breathe-Easy Tank":
        item.click()
        break

driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-167']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-57']").click()
driver.find_element(By.XPATH, "//button[@title='Add to Cart']").click()

wait = WebDriverWait(driver, 40)
#wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@class='action showcart']/span[1]")))
#wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='counter-number']")))
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='action showcart']/span[1]")))

#driver.execute_script("window.scrollTo(0,10);")

#driver.find_element(By.XPATH, "//span[@class='counter-number']").click()


#driver.close()