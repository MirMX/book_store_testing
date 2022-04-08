import pytest
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


@pytest.mark.usefixtures("get_chrome")
class BaseTest:
    pass


class ScreenShot(BasePage):

    def allure_screenshot(self):
        self.do_allure_scrshot(self.do_get_title())


class GoShop(BasePage):

    SHOP = (By.LINK_TEXT, "Shop")

    def go_to_shop_page(self):
        self.do_wait_click(self.SHOP)
