from selenium.webdriver.common.by import By


class RegisterPage_Locators:
    # define locators
    FIRSTNAME_INPUT = (By.NAME, "firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    SUBSCRIBE_RADIO_BUTTON = (By.CSS_SELECTOR, ".form-horizontal .radio-inline:nth-of-type(1) [type]")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "[type='checkbox']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
