import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from Pages.HomePage import HomePage
from Pages.RegPage import RegPage


class AndroidQuickStartPage(BasePage):

    OLD_BOOK_PRICE = (By.XPATH, "//del/span")
    NEW_BOOK_PRICE = (By.XPATH, "//ins/span")
    BOOK_COVER = (By.CLASS_NAME, "wp-post-image")
    BOOK_COVER_CLOSE = (By.CLASS_NAME, "pp_close")
    def __init__(self, driver):
        super().__init__(driver)

# ---------------------------------------------------------------------------- #

    def get_old_book_price(self):
        old_book_price = self.do_wait_visible_text(self.OLD_BOOK_PRICE)
        return old_book_price
    
    def get_new_book_price(self):
        new_book_price = self.do_wait_visible_text(self.NEW_BOOK_PRICE)
        print(new_book_price)
        return new_book_price
    
    def book_cover(self):
        self.do_wait_click(self.BOOK_COVER)
        self.do_wait_click(self.BOOK_COVER_CLOSE)
# ------------------------------------
