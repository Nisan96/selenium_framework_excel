import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage():
    def __init__(self,control):
        self.control = control

    def wait_for_element(self,by,value,timeout=10):
        return WebDriverWait(self.control,timeout).until(ec.visibility_of_element_located((by,value)))

    def click_element(self,by,value):
        element = self.wait_for_element(by,value)
        element.click()

    def input_text(self,by,value,text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def capture_screenshot(self,screenshot_name):
        screenshot_file_path = "D:\\Automation_testing\\selenium_framework\\POM\\screenshots"
        self.control.get_screenshot_as_file(screenshot_file_path + "\\" + screenshot_name + ".png")

