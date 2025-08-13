import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome or firefox or edge or safari")

@pytest.fixture(scope="module")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
         driver = webdriver.Chrome()
    elif browser == "firefox":
         driver = webdriver.Firefox()
    elif browser == "safari":    
         driver= webdriver.Safari()
    elif browser == "edge":
         driver= webdriver.Edge()    
    else:
        raise ValueError(f"Unrecognized browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


