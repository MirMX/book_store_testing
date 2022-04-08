from collections import namedtuple
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from Pages.HomePage import HomePage
from Pages.RegPage import RegPage


class CheckoutPage(BasePage):
    
    FIRST_NAME = (By.ID, "billing_first_name")
    LAST_NAME = (By.ID, "billing_last_name")
    EMAIL_NAME = (By.ID, "billing_email")
    PHONE_NAME = (By.ID, "billing_phone")
    COUNTRY_SELECTOR = (By.ID, "select2-chosen-1")
    COUNTRY_ENTER =(By.ID, "s2id_autogen1_search")
    SELECT_MATCH = (By.CLASS_NAME, "select2-match")
    
    ADDRESS_NAME = (By.ID, "billing_address_1")
    CITY_NAME = (By.ID, "billing_city")
    PROVINCE_SELECTOR = (By.XPATH, "//*[contains(text(), 'Select an option…')]")
    PROVINCE_ENTER = (By.CSS_SELECTOR, "#select2-drop input")
    POSTALCODE_NAME = (By.ID, "billing_postcode")
    PAYMENT_METHOD = (By.ID, "payment_method_cheque")
    PLACE_ORDER_BTN = (By.ID, "place_order")
    CONFIRM_TEXT = (By.XPATH, "//p[contains(text(), 'Thank you.')]")
    CHECK_PAYMENTS = (By.XPATH, "//*[text()='Check Payments']")
    
# ---------------------------------------------------------------------------- #
    def __init__(self, driver):
        super().__init__(driver)

# ---------------------------------------------------------------------------- #

    def place_order(self):
        self.do_wait_send_keys(self.FIRST_NAME, TestData.FIRST_NAME)
        self.do_wait_send_keys(self.LAST_NAME, TestData.LAST_NAME)
        self.do_wait_send_keys(self.EMAIL_NAME, TestData.EMAIL_NAME)
        self.do_wait_send_keys(self.PHONE_NAME, TestData.PHONE_NAME)
        
        self.do_wait_click(self.COUNTRY_SELECTOR)
        self.do_wait_send_keys(self.COUNTRY_ENTER, TestData.COUNTRY)
        self.do_wait_click(self.SELECT_MATCH)
        
        self.do_wait_send_keys(self.ADDRESS_NAME, TestData.ADDRESS_NAME)
        self.do_wait_send_keys(self.CITY_NAME, TestData.CITY_NAME)
        
        self.do_wait_click(self.PROVINCE_SELECTOR)
        self.do_wait_send_keys(self.PROVINCE_ENTER, TestData.PROVINCE)
        self.do_wait_click(self.SELECT_MATCH)
        
        self.do_wait_send_keys(self.POSTALCODE_NAME, TestData.POSTALCODE_NAME)
        
        self.do_scroll(TestData.PIX_VERT_600)
        self.do_wait_click(self.PAYMENT_METHOD)
        self.do_wait_click(self.PLACE_ORDER_BTN)
        
        confirm_text = self.do_wait_visible_text(self.CONFIRM_TEXT)
        check_pay = self.do_wait_all_visible(self.CHECK_PAYMENTS)
        return confirm_text, check_pay
        
        
# --------------------------------------
