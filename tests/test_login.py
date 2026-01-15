from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_valid_login():
    # Setup for the selenium webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com")

    # Testing steps
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    time.sleep(2)

    # Assertion check to check if a specific page is in our test site
    assert "inventory.html" in driver.current_url, "Page not found"

    # Cleaning up
    driver.quit()
    print("Test passed!")

if __name__ == "__main__":
    test_valid_login()