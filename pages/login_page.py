from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # ================= LOCATORS =================
    USER_ID = (By.XPATH, '//*[@id="LoginForm"]/div[1]/input')
    PASSWORD = (By.XPATH, '//*[@id="UserPassword"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="LoginForm"]/div[5]/button')

    REMEMBER_ME = (By.XPATH, '//input[@type="checkbox"]')
    PASSWORD_EYE = (By.XPATH, '//*[@id="password-addon"]')

    INVALID_MSG = (By.XPATH, '//*[@id="LoginForm"]/div[4]')

    # ================= ACTIONS =================

    def enter_user_id(self, user):
        self.driver.find_element(*self.USER_ID).clear()
        self.driver.find_element(*self.USER_ID).send_keys(user)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def click_remember_me(self):
        self.driver.find_element(*self.REMEMBER_ME).click()

    def is_remember_selected(self):
        return self.driver.find_element(*self.REMEMBER_ME).is_selected()

    def click_password_eye(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.PASSWORD_EYE)
        )
        element.click()

    # ================= VALIDATIONS =================

    def get_invalid_message(self):
        return self.driver.find_element(*self.INVALID_MSG).text

    def get_password_type(self):
        return self.driver.find_element(*self.PASSWORD).get_attribute("type")