from collections import namedtuple
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from Pages.HomePage import HomePage
from Pages.RegPage import RegPage


class HtmlPage(BasePage):

    BOOKS_QTY = (By.XPATH, "//li[contains(@class, 'post-')]")
    HTML_QTY = (By.XPATH, "//ul[@class='product-categories']/li[2]/span")

    def __init__(self, driver):
        super().__init__(driver)

    def check_books_quantity(self):
        Qty = namedtuple('qty', ['books_qty', 'html_qty'])
        qty = Qty(books_qty=self.do_find_elements_len(self.BOOKS_QTY),
                  html_qty=self.do_get_number_from_str(self.HTML_QTY))
        return qty
