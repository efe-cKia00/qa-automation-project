import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

class TestLogin:

    @pytest.fixture
    def setup(self):
        """Setup that runs before each test"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        # Teardown - runs after each test
        self.driver.quit()

    def test_error_messages_for_invalid_credentials(self, setup):
        login_page = LoginPage(self.driver)
        login_page.open()

        # Test 1: Wrong username
        login_page.login("wrong_user", "sectret_sauce")
        assert login_page.is_error_message_displayed(), "Error message should be displayed for wrong username"
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text, "Error message should contain 'Epic sadfacee'"
        assert "do not match" in error_text, "Error should mention credentials don't match"

        # Refresh page for next test
        self.driver.refresh()

        # Test 2: Wrong password
        login_page.login("standard_user", "wrong_password")
        assert login_page.is_error_message_displayed(), "Error message should be displayed for wrong password"
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text, "Error message should contain 'Epic sadface'"

        # Refresh page for next test
        self.driver.refresh()

        # Test 3: Locked out user
        login_page.login("locked_out_user", "secret_sauce")
        assert login_page.is_error_message_displayed(), "Error message should be displayed for locked user"
        error_text = login_page.get_error_message()
        assert "locked out" in error_text, "Error should mention user is locked out"

        # Refresh page for next test
        self.driver.refresh()

        # Test 4: Empty username
        login_page.login("", "sectret_sauce")
        assert login_page.is_error_message_displayed(), "Error message should be displayed for empty username"
        error_text = login_page.get_error_message()
        assert "Username is required" in error_text, "Error should mention username is required"

        # Refresh page for next test
        self.driver.refresh()

        # Test 5: Empty password
        login_page.login("standard_user", "")
        assert login_page.is_error_message_displayed(), "Error message should be displayed for the empty password field"
        error_text = login_page.get_error_message()
        assert "Password is required" in error_text, "Error shoud mention password is required"

        # Refresh page for next test
        self.driver.refresh()

        # Test 6: Empty fields
        login_page.login("", "")
        assert login_page.is_error_message_displayed(), "Error message should be displayed for empty username"
        error_text = login_page.get_error_message()
        assert "Username is required" in error_text, "Error should mention username is required"