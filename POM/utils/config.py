import os
import logging

Register_url = "https://tutorialsninja.com/demo/index.php?route=account/register"

Browser = "edge"



LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_FILENAME_VALID = os.path.join(os.getcwd(),'POM', 'RegisterPage_Test_Log', 'validTest_RegisterPage.log')
LOGGING_FILENAME_INVALID = os.path.join(os.getcwd(),'POM', 'RegisterPage_Test_Log', 'invalidTest_RegisterPage.log')
logger = logging.getLogger(__name__)
#logger.setLevel(LOGGING_LEVEL)
formatter = logging.Formatter(LOGGING_FORMAT)