from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

class TestLogin:

    def test_invalid_login(self, driver):

        driver.get("http://119.148.31.69:8050/kroy/")

        login = LoginPage(driver)

        login.enter_user_id("2389542")
        login.enter_password("29823")
        login.click_login()

        assert "dashboard" not in driver.current_url.lower()

        error = driver.find_element("xpath", '//*[@id="LoginForm"]/div[4]').text
        assert error != "Invalid Password."

        time.sleep(4)



    def test_remember_me(self, driver):
        driver.get("http://119.148.31.69:8050/kroy/")

        login = LoginPage(driver)

        login.click_remember_me()

        assert login.is_remember_selected() == True
        time.sleep(5)

    def test_password_visibility_toggle(self, driver):
        driver.get("http://119.148.31.69:8050/kroy/")

        login = LoginPage(driver)

        login.enter_password("123456")

        assert login.get_password_type() == "password"

        login.click_password_eye()

        WebDriverWait(driver, 5).until(
            lambda d: login.get_password_type() == "text"
        )

        assert login.get_password_type() == "text"


    def test_valid_login(self, driver):

        # IMPORTANT: no new browser → same session

        driver.get("http://119.148.31.69:8050/kroy/")

        login = LoginPage(driver)

        login.enter_user_id("101047")
        login.enter_password("132")
        login.click_login()

        time.sleep(5)
        assert driver.current_url == "http://119.148.31.69:8050/kroy/dashboard"
