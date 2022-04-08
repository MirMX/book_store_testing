from collections import namedtuple
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData

class ShopPage(BasePage):

    HTML5_FORM = (By.XPATH, "//h3[text()='HTML5 Forms']")
    HTML_LINK = (By.XPATH, "//a[text()='HTML']")
    BOOKS = (By.XPATH, "//li[contains(@class, 'post-')]")

    SORT_SELECTOR = (By.XPATH, "//option[@value='menu_order']")
    ATTR = "selected"

    SELECTOR = (By.CSS_SELECTOR, "select.orderby")
    VALUE_H_L = ("price-desc")

    SORT_SELECTOR_H_L = (By.XPATH, "//option[@value='price-desc']")

    ANDROID_QUICK_START = (
        By.XPATH, "//h3[text() ='Android Quick Start Guide']")

    HTML5_WEBAPP = (By.XPATH, "//a[@data-product_id='182']")
    JS_DATA = (By.XPATH, "//a[@data-product_id='180']")
    CART = (By.XPATH, "//a[@class='wpmenucart-contents']")
    CART_ITEM = (By.XPATH, "//span[@class='cartcontents']")
    CART_PRICE = (By.XPATH, "//span[@class='amount']")
    CART_ITEM_VALUE = "1 Item"
    CART_PRICE_VALUE = "₹180.00"

    def __init__(self, driver):
        super().__init__(driver)

# >--------------------------- just an example ------------------------------- #
    def check_wait_title_shop(self, title, time=5):
        return self.do_wait_title(title, time)
# >--------------------------------------------------------------------------- #

    def go_to_html5_form_page(self):
        self.do_wait_click(self.HTML5_FORM)
# ---------------------------------------------------------------------------- #

    def go_to_html_page(self):
        self.do_wait_click(self.HTML_LINK)
# ---------------------------------------------------------------------------- #

    def sorting_value(self):
        val = self.do_get_attr(self.SORT_SELECTOR, self.ATTR)
        return val

    def sort_high_to_low(self):
        self.do_get_selector(self.SELECTOR, self.VALUE_H_L)
        val = self.do_get_attr(self.SORT_SELECTOR_H_L, self.ATTR)
        return val
# ---------------------------------------------------------------------------- #

    def go_to_android_quick_start(self):
        self.do_wait_click(self.ANDROID_QUICK_START)
# ---------------------------------------------------------------------------- #
    def add_book(self):
        self.do_wait_click(self.HTML5_WEBAPP)

    def check_item_and_price(self):
        self.do_wait_txt_present(self.CART_ITEM, self.CART_ITEM_VALUE)
        self.do_wait_txt_present(self.CART_PRICE, self.CART_PRICE_VALUE)
        Cart = namedtuple('cart', ['item', 'price'])
        cart = Cart(item=self.do_wait_visible_text(self.CART_ITEM),
                    price=self.do_wait_visible_text(self.CART_PRICE))
        return cart
# ---------------------------------------------------------------------------- #
    def go_to_the_cart(self):
        self.do_wait_click(self.CART)
# ---------------------------------------------------------------------------- #
    def scroll_add_html5webapp_jsdata_go_cart(self):
        self.do_scroll(TestData.PIX_VERT_300)
        self.do_wait_click(self.HTML5_WEBAPP)
        time.sleep(1)
        self.do_wait_click(self.JS_DATA)
        self.go_to_the_cart()
# --------------------------------------------------------------------------- #

    def scroll_add_html5webapp_go_cart(self):
        self.do_scroll(TestData.PIX_VERT_300)
        self.do_wait_click(self.HTML5_WEBAPP)
        self.go_to_the_cart()
# --------------------------------------------------------------------------- #