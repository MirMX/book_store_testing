import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from Base.data import TestData


# ---------------------------------------------------------------------------- #
#                   *   Loading Chrome Profile for testing   *                 #
# ---------------------------------------------------------------------------- #
@pytest.fixture(params=["chrome"], scope="class")
def get_chrome(request):
    if request.param == "chrome":
        profile_1 = r'f:\___QA\Chrome_Profiles\Test_Profile_1'  # !=
        options = Options()
        options.add_argument('user-data-dir=' + profile_1)  # !=
        # options.add_argument('--headless')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.get(TestData.HOME_PAGE_URL)
    yield driver
    driver.quit()



