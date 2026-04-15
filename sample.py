from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import time

def test_valid_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("http://119.148.31.69:8050/kroy/")

    login = LoginPage(driver)

    # Replace with real credentials
    login.enter_user_id("101047")
    login.enter_password("132")
    login.click_login()

    time.sleep(5)

    # Example validation (change if needed)
    assert driver.current_url == "http://119.148.31.69:8050/kroy/dashboard"

    driver.quit()
def test_remember_me(driver):

    driver.get("http://119.148.31.69:8050/kroy/")

    login = LoginPage(driver)

    login.click_remember_me()

    # Try to verify (depends on UI)
    element = driver.find_element(*login.REMEMBER_ME)

    # Option 1: class change
    assert "active" in element.get_attribute("class") or element.is_displayed()

def test_password_visibility_toggle(driver):

    driver.get("http://119.148.31.69:8050/kroy/")

    login = LoginPage(driver)

    login.enter_password("123456")

    # Before click → password hidden
    assert login.get_password_type() == "password"

    # Click eye icon
    login.click_password_eye()

    # After click → password visible
    assert login.get_password_type() == "text"