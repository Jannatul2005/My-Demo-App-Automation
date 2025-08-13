from packages.import_packages import *

@pytest.fixture(scope="module")
def driver():
    capabilities = {
  "platformName": "Android",
  "appium:platformVersion": "16",
  "appium:deviceName": "3A101FDJG0032G",
  "appium:app": "D://automation/My_Demo_App.apk",
  "appium:automationName": "UiAutomator2",
  "appium:noReset": True
}

    appium_options = AppiumOptions()
    appium_options.load_capabilities(capabilities)
    # driver_instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=appium_options)
    driver_instance = webdriver.Remote("http://127.0.0.1:4723", options=appium_options)
    yield driver_instance
    driver_instance.quit()