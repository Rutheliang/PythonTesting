import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_searchAddFlight(self):

        if self.driver.find_element(By.XPATH, "//div[@class='ot-sdk-container']").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, "div[id='onetrust-close-btn-container']").click()

        if self.driver.find_element(By.XPATH, "//div[@class='Box-s8oj9r-0 hzaPoz']").is_displayed():
            self.driver.find_element(By.XPATH, "//img[@alt='closeIcon']").click()

        self.driver.find_element(By.XPATH, "//div[@data-hook='flight-search-origin']").click()

        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element(By.XPATH, "//div[@data-hook='flight-search-origin_AUS']")).click().perform()

        self.driver.find_element(By.XPATH, "//div[@data-hook='flight-search-destination']").click()
        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element(By.XPATH, "//div[@data-hook='flight-search-destination_AVL']")).click().perform()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-hook='flight-search-date-picker_expand-start-date']").click()

        time.sleep(2)
        dates = self.driver.find_elements(By.XPATH, "//div[@data-hook='flight-search-date-picker_calendar-0']/div[3]/button")
        for date in dates:
            if date.get_attribute("data-hook") == "flight-search-date-picker_calendar-0_select-day-24":
                date.click()
                break

        time.sleep(2)
        dates = self.driver.find_elements(By.XPATH, "//div[@data-hook='flight-search-date-picker_calendar-1']/div[3]/button")
        for date in dates:
            if date.get_attribute("data-hook") == "flight-search-date-picker_calendar-1_select-day-24":
                date.click()
                break

        self.driver.find_element(By.XPATH, "//button[@data-hook='flight-search-submit']").click()

        self.driver.find_element(By.XPATH, "//button[@data-hook='flights-page_continue']").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@data-hook='select-tier-1']").click()

        self.driver.find_element(By.XPATH, "//button[@data-hook='bundles-page_continue']").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[id='adults.0.first-name']")))
        self.driver.find_element(By.CSS_SELECTOR, "input[id='adults.0.first-name']").send_keys("Test")

        self.driver.find_element(By.ID, "adults.0.last-name").send_keys("One")
        self.driver.find_element(By.CSS_SELECTOR, "label[data-hook='travelers-form_adults_0_gender_FEMALE']").click()

        self.driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-month']").click()
        self.driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-month_4']").click()

        self.driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-day']").click()
        self.driver.find_element(By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-day_24']").click()

        self.driver.find_element(By.ID, "adults.0.dob-year").send_keys("1985")

        self.driver.find_element(By.ID, "adults.0.email").send_keys("test123@aolc.om")
