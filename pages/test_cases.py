from utils.driver import *
# from pages.Login import *


@pytest.mark.order(1)
def test_details(driver):
    # Catalog
    sidebar = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="open menu"]/android.widget.ImageView')
    sidebar.click()
    time.sleep (3)

    catalog = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')
    catalog.click()
    time.sleep(3)

    #sort by name
    filter = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="sort button"]/android.widget.ImageView')
    filter.click()
    time.sleep(3)

    sort_name = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Name - Ascending"]')
    sort_name.click()
    time.sleep(3)

    #sort by price
    filter = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="sort button"]/android.widget.ImageView')
    filter.click()
    time.sleep(3)

    sort_price = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Price - Ascending"]')
    sort_price.click()
    time.sleep(3)

    # 2nd product
    second_product = driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="store item"])[2]/android.view.ViewGroup[1]/android.widget.ImageView')
    second_product.click()
    time.sleep(2)

    #add to cart 2 
    add_to_cart_2 = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="counter plus button"]/android.widget.ImageView')
    add_to_cart_2.click()
    
    time.sleep(5)

    cart_add = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Add To Cart button"]')
    cart_add.click()
    time.sleep(2)



