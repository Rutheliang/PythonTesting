import time
import cfscrape
import cloudscraper
import certifi

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64 (3)/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.implicitly_wait(5)
certificate_bundle_path = certifi.where()
driver.maximize_window()
driver.get("https://www.allegiantair.com/")

time.sleep(10)


if driver.find_element(By.XPATH, "//div[@class='ot-sdk-container']").is_displayed():
    driver.find_element(By.CSS_SELECTOR, "div[id='onetrust-close-btn-container']").click()

if driver.find_element(By.XPATH, "//div[@class='Box-s8oj9r-0 hzaPoz']").is_displayed():
    driver.find_element(By.XPATH, "//img[@alt='closeIcon']").click()


driver.find_element(By.XPATH, "//div[@data-hook='flight-search-origin']").click()

time.sleep(2)
origins = driver.find_elements(By.CSS_SELECTOR, "div[data-hook*='flight-search-origin']")
for origin in origins:
    origin_state = origin.find_element(By.CSS_SELECTOR, "div")
    if origin_state.text == "Austin, TX (AUS)":
        origin_state.click()
        break

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@data-hook='flight-search-date-picker_expand-start-date']")))
driver.find_element(By.XPATH, "//div[@data-hook='flight-search-destination']").click()

time.sleep(2)
destinations = driver.find_elements(By.CSS_SELECTOR, "div[data-hook*='flight-search-destination']")
for destination in destinations:
    destination_state = destination.find_element(By.CSS_SELECTOR, "div")
    if destination_state.text == "Asheville, NC (AVL)":
        destination_state.click()
        break

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@data-hook='flight-search-destination']")))
driver.find_element(By.XPATH, "//button[@data-hook='flight-search-date-picker_expand-start-date']").click()

driver.find_element(By.XPATH, "//button[@data-hook='flight-search-date-picker_calendar-0_select-day-29']").click()

driver.find_element(By.XPATH, "//button[@data-hook='flight-search-date-picker_calendar-1_select-day-2']").click()

driver.find_element(By.XPATH, "//button[@data-hook='flight-search-submit']").click()

driver.find_element(By.XPATH, "//button[@data-hook='flights-page_continue']").click()

time.sleep(2)
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
