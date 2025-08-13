
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
# from selenium.webdriver.support import expected_conditions as EC
import time
 

# Desired capabilities
capabilities = {
  "platformName": "Android",
  "platformVersion": "14",
  "deviceName": "RZ8W800X1WW",
  "appium:app": "D://demo_apps/cashbaba_demo_4.0.13_261.apk",
  "automationName": "UiAutomator2",
#   "noReset": True
}

# To avoid conflict between versions
appium_options = AppiumOptions()
appium_options.load_capabilities(capabilities)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=appium_options)
appium_options.no_reset = True
appium_options.full_reset = False


# current_package = driver.current_package
# print(f"Current Package: {current_package}")

# current_activity = driver.current_activity
# print(f"Current Activity: {current_activity}")
print("Started")
time.sleep(5)

login_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Log in"]')
login_button.click()
print("Login button clicked successfully!")
time.sleep(5)

# credential
mobile = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile']")
password = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")
time.sleep(5)

# input value
mobile.send_keys("01786695785")
password.send_keys("Password1@")
time.sleep(5)

LogIn = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc="Log in"])
LogIn.click()

time.sleep(5) # load Dashboard

# click on add money
add_money = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView[3]')
add_money.click()
time.sleep(5)
# print("Started")