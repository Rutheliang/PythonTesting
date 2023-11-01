import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64 (4)/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(15)

driver.maximize_window()
driver.get("https://www.allegiantair.com/")

if driver.find_element(By.XPATH, "//div[@class='ot-sdk-container']").is_displayed():
    driver.find_element(By.CSS_SELECTOR, "div[id='onetrust-close-btn-container']").click()

if driver.find_element(By.XPATH, "//div[@class='Box-s8oj9r-0 hzaPoz']").is_displayed():
    driver.find_element(By.XPATH, "//img[@alt='closeIcon']").click()


driver.find_element(By.XPATH, "//div[@data-hook='flight-search-origin']").click()

#wait = WebDriverWait(driver, 10)
#wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@data-hook='flight-search-origin_AUS']")))
#driver.find_element(By.XPATH, "//div[@data-hook='flight-search-origin_AUS']").click()

time.sleep(2)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//div[@data-hook='flight-search-origin_AUS']")).click().perform()
#action.move_to_element(driver.find_element(By.XPATH, "//div[@id='react-select-origin-option-1-5']")).click().perform()

#time.sleep(2)
driver.find_element(By.XPATH, "//div[@data-hook='flight-search-destination']").click()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//div[@data-hook='flight-search-destination_AVL']")).click().perform()

#wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.element_located_to_be_selected((By.XPATH, "//button[@data-hook='flight-search-date-picker_expand-start-date']")))

time.sleep(2)
driver.find_element(By.XPATH, "//button[@data-hook='flight-search-date-picker_expand-start-date']").click()

time.sleep(2)
dates = driver.find_elements(By.XPATH, "//div[@data-hook='flight-search-date-picker_calendar-0']/div[3]/button")
for date in dates:
    if date.get_attribute("data-hook") == "flight-search-date-picker_calendar-0_select-day-26":
        date.click()
        break

time.sleep(2)
dates = driver.find_elements(By.XPATH, "//div[@data-hook='flight-search-date-picker_calendar-1']/div[3]/button")
for date in dates:
    if date.get_attribute("data-hook") == "flight-search-date-picker_calendar-1_select-day-2":
        date.click()
        break

driver.find_element(By.XPATH, "//button[@data-hook='flight-search-submit']").click()

driver.find_element(By.XPATH, "//button[@data-hook='flights-page_continue']").click()

time.sleep(3)
driver.find_element(By.XPATH, "//button[@data-hook='select-tier-1']").click()

driver.find_element(By.XPATH, "//button[@data-hook='bundles-page_continue']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[id='adults.0.first-name']")))
driver.find_element(By.CSS_SELECTOR, "input[id='adults.0.first-name']").send_keys("Test")

driver.find_element(By.ID, "adults.0.last-name").send_keys("One")
driver.find_element(By.CSS_SELECTOR, "label[data-hook='travelers-form_adults_0_gender_FEMALE']").click()

driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-month']").click()
driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-month_4']").click()

driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-day']").click()
driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-day_24']").click()

driver.find_element(By.ID, "adults.0.dob-year").send_keys("1985")

driver.find_element(By.ID, "adults.0.email").send_keys("test123@aolc.om")

driver.find_element(By.XPATH, "//button[@data-hook='travelers-page_continue']").click()
driver.close()
