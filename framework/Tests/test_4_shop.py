import allure
import pytest
from Base.data import TestData
from Pages.AndroidQuickStartPage import AndroidQuickStartPage
from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
from Pages.Html5_FormsPage import Html5Page
from Pages.HtmlPage import HtmlPage
from Pages.LoginPage import LoginPage
from Pages.ShopPage import ShopPage
from Tests.test_base import BaseTest, GoShop
from Tests.test_base import ScreenShot

# >--------------------------------------------------------------------------- #


class LoginShop():

    def login_go_shop(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()
        self.testPage = GoShop(self.driver)
        self.testPage.go_to_shop_page()
        self.shopPage = ShopPage(self.driver)

    def go_shop(self):
        self.testPage = GoShop(self.driver)
        self.testPage.go_to_shop_page()
        self.shopPage = ShopPage(self.driver)

    def allure_ss(self):
        self.scrShot = ScreenShot(self.driver)
        self.scrShot.allure_screenshot()

# >--------------------------------------------------------------------------- #

# @pytest.mark.skip
class Test_Shop_04(BaseTest, LoginShop):

    @allure.severity(allure.severity_level.MINOR)
    def test_04_display_product_title(self):
        self.login_go_shop()
        self.shopPage.go_to_html5_form_page()
        self.html5Page = Html5Page(self.driver)
        book_title = self.html5Page.check_book_title()
        print(f"\nBook title is {book_title}")
        assert book_title == TestData.BOOK_TITLE_HTML5_FORM


# @pytest.mark.skip
class Test_Shop_05(BaseTest, LoginShop):

    def test_05_products_quantity_in_category(self):
        self.login_go_shop()
        self.shopPage.go_to_html_page()
        self.htmlPage = HtmlPage(self.driver)
        exp_qty = 3
        qty = self.htmlPage.check_books_quantity()
        print(f"\n\n1. The Quantity of Products by presented amount on the page: {qty.books_qty}"
              f"\n2. The Quantity of by shown amount in PRODUCT CATEGORIES: {qty.html_qty}"
              f"\nExpected Result: {exp_qty}")
        self.allure_ss()
        assert qty.books_qty == qty.html_qty == exp_qty


# @pytest.mark.skip
class Test_Shop_06(BaseTest, LoginShop):

    def test_06_1_product_sorting(self):
        self.login_go_shop()
        select_value = self.shopPage.sorting_value()
        print(
            f"\n4 Step - Selection set to \'Default sorting\': {select_value}")
        self.allure_ss()
        assert select_value

    def test_06_2_product_sorting(self):
        self.shopPage = ShopPage(self.driver)
        select_value = self.shopPage.sort_high_to_low()
        print(
            f"\n7 Step - Selection set to \'Sort by price: high to low\': {select_value}")
        self.allure_ss()
        assert select_value


# @pytest.mark.skip
class Test_Shop_07(BaseTest, LoginShop):

    def test_07_old_book_price(self):
        self.login_go_shop()
        self.shopPage.go_to_android_quick_start()
        self.androidQuickstart = AndroidQuickStartPage(self.driver)
        exp_old_book_price = "₹600.00"
        old_book_price = self.androidQuickstart.get_old_book_price()
        print("\n--- 5 Step (assert Old Price) ---")
        print(f"The Old Price Rusult: {old_book_price}"
              f"\nExpected Old Price Result: {exp_old_book_price}")
        print("---------------------------------")
        self.allure_ss()
        assert old_book_price == exp_old_book_price

    def test_07_new_book_price(self):
        self.androidQuickstart = AndroidQuickStartPage(self.driver)
        exp_new_book_price = "₹450.00"
        new_book_price = self.androidQuickstart.get_new_book_price()
        print("\n--- 6 Step (assert New Price) ---")
        print(f"The New Price Rusult: {new_book_price}"
              f"\nExpected New Price Result: {exp_new_book_price}")
        print("---------------------------------")
        self.allure_ss()
        assert new_book_price == exp_new_book_price

    def test_07_book_cover_wait(self):
        self.androidQuickstart = AndroidQuickStartPage(self.driver)
        self.androidQuickstart.book_cover()
        assert True


# @pytest.mark.skip
class Test_Shop_08(BaseTest, LoginShop):

    def test_08_1_check_item_in_the_cart(self):
        self.go_shop()
        self.shopPage.add_book()
        cart = self.shopPage.check_item_and_price()
        exp_cart_item = "1 Item"
        print("\n--- 4 Step (assert Items amount & Price) ---")
        print("Rusult:\n"
              f"The Items amount: {cart.item}"
              "\n\nExpected Result:\n"
              f"The Items amount: {exp_cart_item}")
        self.allure_ss()
        assert cart.item == exp_cart_item

    def test_08_2_check_price_in_the_cart(self):
        self.shopPage = ShopPage(self.driver)
        cart = self.shopPage.check_item_and_price()
        exp_cart_price = "₹180.00"
        print("\nRusult:\n"
              f"The Price: {cart.price}"
              "\n\nExpected Result:\n"
              f"The Price: {exp_cart_price}")
        print("--------------------------------------------")
        self.allure_ss()
        assert cart.price == exp_cart_price

    def test_08_3_check_subtotal(self):
        self.shopPage = ShopPage(self.driver)
        self.shopPage.go_to_the_cart()
        self.cartPage = CartPage(self.driver)
        exp_cart_subtotal = "₹180.00"
        exp_cart_total = "₹189.00"
        cart = self.cartPage.check_subtotal()
        print(cart)
        self.allure_ss()
        assert (cart.subtotal == exp_cart_subtotal) and (
            cart.total == exp_cart_total)


# @pytest.mark.skip
class Test_Shop_09(BaseTest, LoginShop):

    def test_09_1_assert_qty_in_the_cart(self):
        self.go_shop()
        self.shopPage.scroll_add_html5webapp_jsdata_go_cart()
        self.cartPage = CartPage(self.driver)
        exp_book_jsdata_value = "3"
        book_jsdata_value = self.cartPage.remove_undo_set_js_data_qty()
        print("\n--- 9 Step - assert quantity of \'JS Data Structures and Algorithm\' ---")
        print(f"\nRusult: {book_jsdata_value}"
              f"\nExpected Result: {exp_book_jsdata_value}")
        print("------------------------------------------------------------------------")
        self.allure_ss()
        assert book_jsdata_value == exp_book_jsdata_value

    def test_09_2_assert_coupon_msg(self):
        self.cartPage = CartPage(self.driver)
        coupon_msg = self.cartPage.coupon_msg()
        exp_coupon_msg = "Please enter a coupon code."
        print("\n--- 11 Step - assert message \'Please enter a coupon code.\'---")
        print(f"\nRusult: {coupon_msg}"
              f"\nExpected Result: {exp_coupon_msg}")
        print("------------------------------------------------------------------------")
        self.allure_ss()
        assert coupon_msg == exp_coupon_msg


# @pytest.mark.skip
class Test_Shop_10(BaseTest, LoginShop):

    def test_10_shop_buy_the_book(self):
        self.go_shop()
        self.shopPage.scroll_add_html5webapp_go_cart()
        self.cartPage = CartPage(self.driver)
        self.cartPage.go_proceed_to_checkout()
        self.checkoutPage = CheckoutPage(self.driver)
        values = self.checkoutPage.place_order()
        print(f"\n9 Step - Text: \'{values[0]}\' is visible on the page")
        print(f"\n10 Step - All {values[1]} "
              f"Payment Methods on the page are set to \"Check Payments\"")
        self.allure_ss()
        assert values
