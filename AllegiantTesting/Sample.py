import undetected_chromedriver as uc
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service

chrome_options = uc.ChromeOptions()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


service_obj = Service("/Users/ruthelia/Downloads/chromedriver_mac_arm64 (1)/chromedriver")
driver = uc.Chrome(service=service_obj, options=chrome_options)
driver.get("https://www.allegiantair.com/")
driver.maximize_window()