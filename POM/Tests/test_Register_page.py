import time
import pytest
from selenium import webdriver
from POM.Pages.Register_page import RegisterPage
from POM.Pages.base_page import BasePage
from POM.utils.config import Register_url,Browser

@pytest.fixture           ## Decorator called
def setup():
    if Browser == "edge":
        drive = webdriver.Edge()
    elif Browser == "firefox":
        drive = webdriver.Firefox()
    elif Browser == "chrome":
        drive = webdriver.Chrome()
    else:
        raise ValueError("Unsupported browser:" + Browser)

    drive.get(Register_url)
    drive.maximize_window()

    yield drive
    drive.quit()

def test_RegisterPage_valid(setup):
    register_page = RegisterPage(setup)
    register_page.Register('ashraf','nisan','ash76@gmail.com','01772693406','admin123','admin123')
    register_page.control.implicitly_wait(5)
    register_page.capture_screenshot("RegisterPage_test_valid")
    #time.sleep(3)


def test_RegisterPage_invalid(setup):
    register_page = RegisterPage(setup)
    register_page.Register('123', '456', 'ash96@..gmail.com', '0177269', 'admin123', 'admin1234')
    register_page.control.implicitly_wait(5)
    time.sleep(3)
    register_page.capture_screenshot("RegisterPage_test_invalid")
    #time.sleep(3)
