from selenium.webdriver.common.by import By
from POM.Pages.base_page import BasePage
from POM.utils.locators import RegisterPage_Locators

class RegisterPage(BasePage):
    # define register actions
    def Register(self,firstname,lastname,email,telephone,password,confirm_password):
        self.input_text(*RegisterPage_Locators.FIRSTNAME_INPUT,firstname)
        self.input_text(*RegisterPage_Locators.LASTNAME_INPUT,lastname)
        self.input_text(*RegisterPage_Locators.EMAIL_INPUT, email)
        self.input_text(*RegisterPage_Locators.TELEPHONE_INPUT, telephone)
        self.input_text(*RegisterPage_Locators.PASSWORD_INPUT, password)
        self.input_text(*RegisterPage_Locators.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click_element(*RegisterPage_Locators.SUBSCRIBE_RADIO_BUTTON)
        self.click_element(*RegisterPage_Locators.AGREE_CHECKBOX)
        self.click_element(*RegisterPage_Locators.CONTINUE_BUTTON)




