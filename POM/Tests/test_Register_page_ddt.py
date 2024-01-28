import time
import pytest
from selenium import webdriver
from POM.Pages.Register_page import RegisterPage
from POM.Pages.base_page import BasePage
from POM.Data.RegisterPage_data import Register_test_data
from POM.utils.config import LOGGING_FORMAT,LOGGING_LEVEL,LOGGING_FILENAME_VALID,LOGGING_FILENAME_INVALID,logger,formatter
import logging
from POM.utils.excel_utils import *
import pandas as pd

# Excel file location and sheet number
excel_file = "./POM/Data/RegisterPage_data.xlsx"
sheet_name = "Sheet1"

# list of storing test results
test_results = []

#expected url after clicking continue button
expected_url_validtest = "https://tutorialsninja.com/demo/index.php?route=account/success"
expected_url_invalidtest = "https://tutorialsninja.com/demo/index.php?route=account/register"

# calling function to extract data from different rows of Excel file
read_validtest_data = read_RegisterPage_validtest_data(excel_file,sheet_name).values
read_invalidtest_data = read_RegisterPage_invalidtest_data(excel_file,sheet_name).values

@pytest.mark.parametrize("firstname,lastname,email,telephone,password,confirm_password,expcted_result",
                         [read_validtest_data])
def test_RegisterPage_valid(setup,firstname,lastname,email,telephone,password,confirm_password,expcted_result):
    logger.setLevel(LOGGING_LEVEL)
    file_handler = logging.FileHandler(LOGGING_FILENAME_VALID)
    file_handler.setLevel(LOGGING_LEVEL)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    register_page = RegisterPage(setup)
    register_page.Register(firstname,lastname,email,telephone,password,confirm_password)
    register_page.control.implicitly_wait(5)
    logger.info("Input data done")

    actual_url_validtest = register_page.control.current_url
    if expected_url_validtest == actual_url_validtest:
        test_results.append("validTest Pass")
    else:
        test_results.append("validTest Fail")
    register_page.capture_screenshot("RegisterPage_test_valid")
    logger.info("valid test done")
    #time.sleep(3)
    logger.removeHandler(file_handler)


@pytest.mark.parametrize("firstname,lastname,email,telephone,password,confirm_password,expected_result",
                         [read_invalidtest_data])
def test_RegisterPage_invalid(setup,firstname,lastname,email,telephone,password,confirm_password,expected_result):
    logger.setLevel(LOGGING_LEVEL)
    file_handler = logging.FileHandler(LOGGING_FILENAME_INVALID)
    file_handler.setLevel(LOGGING_LEVEL)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    register_page = RegisterPage(setup)
    register_page.Register(firstname,lastname,email,telephone,password,confirm_password)
    register_page.control.implicitly_wait(5)
    logger.info("Input data done")

    actual_url_invalidtest = register_page.control.current_url
    if expected_url_invalidtest == actual_url_invalidtest:
        test_results.append("invalidTest Pass")
    else:
        test_results.append("invalidTest Fail")
    time.sleep(3)
    register_page.capture_screenshot("RegisterPage_test_invalid")
    logger.info("invalid test done")
    #time.sleep(3)
    logger.removeHandler(file_handler)

# after all tests have run write the test results to the Excel file
@pytest.fixture(scope = "session", autouse = True)
def write_TestResults_to_excel(request):
    def finalize():
        #Load the existing excel file
        existing_data = pd.read_excel(excel_file,sheet_name=sheet_name)
        # add the test results as a new column
        existing_data['Actual Result'] = test_results

        with pd.ExcelWriter(excel_file,engine='openpyxl') as writer:
            existing_data.to_excel(writer,sheet_name=sheet_name,index=False)

    request.addfinalizer(finalize)

