import pytest
from Base.data import TestData
from Pages.HomePage import HomePage
from Pages.SeleniumRubyPage import SeleniumRubyPage
from Tests.test_base import BaseTest

@pytest.mark.skip
class Test_Home(BaseTest):

    def test_home(self):
        self.homePage = HomePage(self.driver)
        self.homePage.scroll_click(TestData.PIX_VERT_600)
        self.rubyPage = SeleniumRubyPage(self.driver)
        self.rubyPage.submitReview()
        assert True
