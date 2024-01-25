import pytest
from selenium import webdriver
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