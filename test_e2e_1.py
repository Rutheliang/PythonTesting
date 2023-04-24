import pytest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from pageObject.CheckoutPage import CheckoutPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup") # optimize in baseclass since this is use in every test
class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()

        products = self. driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()

        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText  # use IN instead of equal for partial words




