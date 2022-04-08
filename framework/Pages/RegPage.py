import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from selenium import webdriver


class RegPage(BasePage):

    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    REG_EMAIL = (By.ID, "reg_email")
    REG_PASS = (By.ID, "reg_password")
    REG_BTN = (By.XPATH, "//input[@name='register']")
    MSG = (By.TAG_NAME, "strong")  # > msg about registration

    def __init__(self, driver):
        super().__init__(driver)

    def regisration(self):
        self.do_wait_click(self.MY_ACCOUNT)
        self.do_wait_send_keys(self.REG_EMAIL, TestData.EMAIL)
        self.do_wait_send_keys(self.REG_PASS, TestData.PASSWORD)
        self.do_simple_click(self.REG_BTN)
        self.do_wait_visible(self.MSG)
        self.do_allure_scrshot(self.do_get_title())
