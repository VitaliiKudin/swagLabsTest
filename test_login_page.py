"""Store tests related to start page"""
from time import sleep

import pytest
from conftest import BaseTest
from selenium import webdriver
from selenium.webdriver.common.by import By

from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from helpers.base import BaseHelpers


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="session")
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(5)
        yield driver
        driver.close()

    def test_sample_login(self, driver):
        """
        - Open start page
        - Clear password and login
        - Click on login button
        - Verify error message
        :param driver:
        :return:

        """
        base_helper = BaseHelpers(driver)
        # Open start page
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")

        # Clear fields
        base_helper.clear_fields(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        base_helper.clear_fields(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        self.log.info("Clear fields")

        # Click login button
        base_helper.click_button(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sleep(3)
        self.log.info("Click button and wait 3 sec")

        # Verify error message
        error_message = driver.find_element_by_xpath(LoginPageConstants.USERNAME_IS_REQUIRED_MESSAGE_XPATH)
        assert error_message.text == LoginPageConstants.USERNAME_IS_REQUIRED_MESSAGE_TEXT
        self.log.info("Error message match to expected")
