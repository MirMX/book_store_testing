from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from Pages.SeleniumRubyPage import SeleniumRubyPage


class HomePage(BasePage):

    SELENIUM_RUBY = (By.XPATH, "//h3[text()='Selenium Ruby']")

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_click(self, PIX_VERT_600):
        # > 2 Scroll 600 pixels
        self.do_scroll(PIX_VERT_600)
        # > 3 Click on "Selenium Ruby --> SeleniumRubyPage"
        self.do_wait_click(self.SELENIUM_RUBY)
