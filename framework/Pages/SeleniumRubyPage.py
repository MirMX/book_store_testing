from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData


class SeleniumRubyPage(BasePage):

    REVIEWS = (By.XPATH, "//a[@href = '#tab-reviews']")
    STARS_5 = (By.CSS_SELECTOR, "a.star-5")
    COMMENT = (By.ID, "comment")
    NAME = (By.ID, "author")
    EMAIL = (By.ID, "email")
    SUBMIT_BTN = (By.ID, "submit")

    def __init__(self, driver):
        super().__init__(driver)

    def submitReview(self):
        self.do_wait_click(self.REVIEWS)
        self.do_wait_click(self.STARS_5)
        self.do_wait_send_keys(self.COMMENT, TestData.COMMENT_REVIEW)
        self.do_wait_send_keys(self.NAME, TestData.NAME_REVIEW)
        self.do_wait_send_keys(self.EMAIL, TestData.EMAIL)
        self.do_allure_scrshot(self.do_get_title())
        self.do_wait_click(self.SUBMIT_BTN)
        self.do_allure_scrshot(self.do_get_title())
