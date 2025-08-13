from utils.driver import *

@pytest.mark.order(1)
def test_loginDetails(driver):
    sidebar = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="open menu"]/android.widget.ImageView')
    sidebar.click()
    time.sleep (3)

    login_option = driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="store item"])[3]/android.view.ViewGroup[1]/android.widget.ImageView')
    login_option.click()
    time.sleep(3)
    


    # Click on Log in
    username = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="Username input field"]')
    # username.click()
    time.sleep (3)
    username.send_keys('bob@example.com')

    password = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="Password input field"]')
    # password.click()
    time.sleep (3)
    password.send_keys('10203040')

    # done_pass= driver.find_element('//android.widget.TextView[@text="Password"][5]')
    # done_pass.click()
    # time.sleep (3)

    submit = driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Login button"]')
    submit.click()
    time.sleep (3)

