from utils.driver import *

def test_loginDetails(driver):
    # Input PIN
    time.sleep(2)
    PIN = driver.find_element(AppiumBy.XPATH, 
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    PIN.click()
    time.sleep(2)

    no_6 = driver.find_element(AppiumBy.XPATH, 
        '//android.view.View[@content-desc="6"]')
    no_6.click()
    time.sleep(2)
    
    no_9 = driver.find_element(AppiumBy.XPATH, 
        '//android.view.View[@content-desc="9"]')
    no_9.click()
    time.sleep(2)

    no_6 = driver.find_element(AppiumBy.XPATH, 
        '//android.view.View[@content-desc="6"]')
    no_6.click()
    time.sleep(2)
    
    no_9 = driver.find_element(AppiumBy.XPATH, 
        '//android.view.View[@content-desc="9"]')
    no_9.click()
    time.sleep(2)
    
    no_5 = driver.find_element(AppiumBy.XPATH, 
        '//android.view.View[@content-desc="5"]')
    no_5.click()
    time.sleep(2)

    # Login Button
    login = driver.find_element(AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[12]')
    login.click()
    time.sleep (3)


