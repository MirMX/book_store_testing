from collections import namedtuple
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Base.data import TestData
from Pages.HomePage import HomePage
from Pages.RegPage import RegPage


class CartPage(BasePage):

    CART_SUBTOTAL = (
        By.XPATH, "//td[@data-title='Subtotal']/span")
    CART_TOTAL = (By.XPATH, "//td[@data-title='Total']/strong/span")

    REMOVE_HTML5_WEBAPP = (By.XPATH, "//a[@*='remove' and @*='182']")
    UNDO = (By.XPATH, "//a[text()='Undo?']")
    QTY_JS_DATA = (By.XPATH, "//input[contains(@name, '045117')]")
    UPDATE_BASKET = (By.XPATH, "//input[@*='Update Basket']")
    BASKET_UPD_MSG = (By.XPATH, "//div[contains(text(), 'Basket updated.')]")
    APPLY_COUPON = (By.XPATH, "//input[@*='Apply Coupon']")
    COUPON_MSG = (By.XPATH, "//li[text()='Please enter a coupon code.']")
    
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[contains(@*, 'checkout')]")
    
# ---------------------------------------------------------------------------- #
    def __init__(self, driver):
        super().__init__(driver)

# >--------------------------------------------------------------------------- #
    def check_subtotal(self):
        Cart = namedtuple('cart', ['subtotal', 'total'])
        cart = Cart(subtotal=self.do_wait_visible_text(self.CART_SUBTOTAL),
                    total=self.do_wait_visible_text(self.CART_TOTAL))
        return cart

    def remove_undo_set_js_data_qty(self):
        self.do_wait_click(self.REMOVE_HTML5_WEBAPP)
        self.do_wait_click(self.UNDO)
        self.do_wait_clear(self.QTY_JS_DATA)
        self.do_wait_send_keys(self.QTY_JS_DATA, "3")
        self.do_wait_click(self.UPDATE_BASKET)
        qty_js_data = self.do_get_attr(self.QTY_JS_DATA, "value")
        return qty_js_data
    
    def coupon_msg(self):
        self.do_wait_txt_present(
            self.BASKET_UPD_MSG, "Basket updated.")
        self.do_wait_click(self.APPLY_COUPON)
        self.do_wait_present(self.COUPON_MSG)
        coupon_msg = self.do_find_element_text(self.COUPON_MSG)
        return coupon_msg

# --------------------------------------------------------------------------- #
    def go_proceed_to_checkout(self):
        self.do_wait_click(self.PROCEED_TO_CHECKOUT)
# --------------------------------------------------------------------------- #