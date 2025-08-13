import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver():
  capabilities = {
  "platformName": "Android",
  "platformVersion": "14",
  "deviceName": "RZ8W800X1WW",
  "appium:app": "D:/demo_apps/cashbaba_demo_4.0.12_261.apk",
  "automationName": "UiAutomator2"
}

  # To avoid conflict between versions
  appium_options = AppiumOptions()
  appium_options.load_capabilities(capabilities)
  driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=appium_options)
    
  print("Started")

    # Connect to Appium server
    # driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    # driver.implicitly_wait(10)
    # yield driver
    # driver.quit()


def test_login_button_and_fields(driver):
    # Wait for the login screen to load
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Log in']"))
    )

    #  Assert the presence of the login button
    login_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Log in']")
    assert login_button.is_displayed(), "Log in button is not visible"

    # Click the login button to navigate to the login page
    login_button.click()

    # Wait for the login input fields to load
    WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile']"))
    )

    # Locate the Mobile and Password input fields
    mobile_field = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile']")
    password_field = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")

    # Assert input fields are visible
    assert mobile_field.is_displayed(), "Mobile input field is not visible"
    assert password_field.is_displayed(), "Password input field is not visible"

    # Enter test credentials
    mobile_field.send_keys("testuser")
    password_field.send_keys("password123")

    # Submit the login form
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Log in']").click()

    # Optionally, wait for the dashboard to load and assert success
    WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Dashboard')]"))
    )

    # assert "Dashboard" in driver.page_source, "Login failed or Dashboard not loaded"
