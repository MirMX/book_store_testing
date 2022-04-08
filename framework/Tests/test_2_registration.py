import pytest
from Pages.RegPage import RegPage
from Tests.test_base import BaseTest

# @pytest.mark.skip
class Test_Registration(BaseTest):
    
    def test_registration(self):
        self.RegPage = RegPage(self.driver)
        self.RegPage.regisration()
        assert True

