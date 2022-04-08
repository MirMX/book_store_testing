from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from Pages.HomePage import HomePage
from Pages.RegPage import RegPage


class Html5Page(BasePage):

    BOOK_TITLE = (By.XPATH, "//h1[text()='HTML5 Forms']")

    def __init__(self, driver):
        super().__init__(driver)

    def check_book_title(self):
        self.do_allure_scrshot(self.do_get_title())
        return self.do_wait_visible_text(self.BOOK_TITLE)
