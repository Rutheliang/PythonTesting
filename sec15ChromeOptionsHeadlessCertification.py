from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# class called chrome options class which you can set the behavior of your browser while invoking
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized") # MAXIMIZE SCREEN (OLD CODE)
# chrome_options.add_argument("headless") # NOT OPEN BROWSER
chrome_options.add_argument("--ignore-certificate-errors") # IGNORE CERTIFICATION ERROR / YOUR CONNECTION IS PRIVATE

service_obj = Service("/Users/ruthelia/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)


driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)