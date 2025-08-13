# import csv
import pytest
# from selenium import webdriver
import time
# from data import test_data
from pages.login_page import login_details
# from pages.Logout_page import Logout
# from pages.takeimage_page import Take_image
# from conftest import driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait



#step1:loging Page
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(1)
# def test_logIn_page(driver):
#   driver.get("https://cgl2024.sslwireless.com/")
#   takeimages=Take_image(driver)
#   takeimages.take_screenshot()
#   loging_page=Loging(driver)
#   loging_page.login_details(
#         test_data.Email,
#         test_data.password
#     )
time.sleep(5)

# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.order(2)
# def test_logout_page(driver):
#     # Assuming the driver is already logged in from previous tests
#   takeimages = Take_image(driver)
#   takeimages.take_screenshot()
#   logout_page = Logout(driver)
#   logout_page.perform_logout(driver)
#   time.sleep(5)
