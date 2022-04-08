from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from Pages.HomePage import HomePage
from Pages.RegPage import RegPage


class LoginPage(BasePage):

    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//input[@name='login']")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.HOME_PAGE_URL)

    def login(self):
        self.do_wait_click(RegPage.MY_ACCOUNT)
        self.do_wait_send_keys(self.LOGIN, TestData.EMAIL)
        self.do_wait_send_keys(self.PASSWORD, TestData.PASSWORD)
        self.do_wait_click(self.LOGIN_BTN)

    def check_logout(self):
        self.do_allure_scrshot(self.do_get_title())
        return self.do_wait_present(self.LOGOUT)
# ---------------------------------------------------------------------------- #


