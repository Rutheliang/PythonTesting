import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument('--headless')
#chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#chrome_options.add_experimental_option('useAutomationExtension', False)
driver = uc.Chrome(use_subprocess=True)

service_obj = Service("/Users/ruthelia/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://www.allegiantair.com/")

if driver.find_element(By.XPATH, "//div[@class='ot-sdk-container']").is_displayed():
    driver.find_element(By.CSS_SELECTOR, "div[id='onetrust-close-btn-container']").click()

if driver.find_element(By.XPATH, "//div[@class='Box-s8oj9r-0 hzaPoz']").is_displayed():
    driver.find_element(By.XPATH, "//img[@alt='closeIcon']").click()


driver.find_element(By.XPATH, "//div[@data-hook='flight-search-origin']").click()