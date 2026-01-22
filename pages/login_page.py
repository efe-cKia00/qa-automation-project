from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        self.driver.get("https://www.saucedemo.com")
    
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """Get the error message text when login fails"""
        error_element = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error_element.text
    
    def is_error_message_displayed(self):
        """Check if error message is visible"""
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error_element.is_displayed()
        except:
            return False