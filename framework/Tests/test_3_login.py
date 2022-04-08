import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

# @pytest.mark.skip
class Test_Login(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()
        presence_true = self.loginPage.check_logout()
        print(f"\nElement \"Logout\" is on the page!: {presence_true}")
        assert presence_true
