from utils.driver import *
from packages.import_packages import *
from data.test_data import *


class Login_details:
    # login_button
    # login_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Log in"]')
    
    # credential
    mobile = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')

    password = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
    
    # input value
    mobile.send_keys(mobileNo)
    password.send_keys(passWord)
  
    LogIn = driver.find_element (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Log in"]')
class Add_Money:
    add_money = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView[3]')
    add_money.click()  
    time.sleep(5)

class Card_to_Wallet:
    CardToWallet = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Card to Wallet Add money from card"]')
    CardToWallet.click() 
    time.sleep(3)

    CardToWallet_sendMoney = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="৳100"]')
    Submit = driver.find_element (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]')
    # LogIn.click()
    time.sleep(3)
    Confirm_Submit = driver.find_element (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]')
    time.sleep(3)

    sandbox_pay = driver.find_element (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.bd_cashbaba:id/tv_pay"]')
    time.sleep(3)

    sandbox_otp = driver.find_element (AppiumBy.XPATH, '//android.webkit.WebView[@resource-id="com.bd_cashbaba:id/bankPage"]')
    time.sleep(5)
    
    go_home = driver.find_element (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Go to Home"]')
    time.sleep(5)
    


    # input value
    # mobile.send_keys("1000")
    time.sleep(5)



class Send_Money:
    send_money = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Add Money]')
    send_money.click()  
    time.sleep(5)

