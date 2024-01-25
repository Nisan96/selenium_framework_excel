from selenium.webdriver.common.by import By

class RegisterPageLocators:
    firstName_field = (By.ID, "input-firstname")
    lastName_field = (By.ID, "input-lastname")
    email_field = (By.ID, "input-email")
    telephone_field = (By.ID, "input-telephone")
    password_field = (By.ID, "input-password")
    confirm_password_field = (By.ID, "input-confirm")
    subscribe_radio_button = (By.XPATH,
                "/html//div[@id='content']/form[@action='https://tutorialsninja.com/demo/index.php?route=account/register']//div[@class='form-group']/div[@class='col-sm-10']/label[1]/input[@name='newsletter']")
    agree_checkbox = (By.CSS_SELECTOR, "[type='checkbox']")
    continue_button = (By.CLASS_NAME, "btn-primary")


