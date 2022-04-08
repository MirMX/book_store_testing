from collections import namedtuple
from selenium.webdriver.support.select import Select
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Templates:
    
    def cond(self):
        Waits = namedtuple('wait_cond', [
            'visible',
            'visible_all',
            'invisible',

            'present',
            'present_all',

            'text_present',
            'text_present_value',

            'clickable',

            'title',
            'title_contains',
        ])
        conds = Waits(
            visible=EC.visibility_of_element_located,
            visible_all=EC.visibility_of_all_elements_located,
            invisible=EC.invisibility_of_element_located,

            present=EC.presence_of_element_located,
            present_all=EC.presence_of_all_elements_located,

            text_present=EC.text_to_be_present_in_element,
            text_present_value=EC.text_to_be_present_in_element_value,

            clickable=EC.element_to_be_clickable,

            title=EC.title_is,
            title_contains=EC.title_contains,
        )
        return conds
# ---------------------------------------------------------------------------- #
#                           WebDriverWait - Templates                          #
# ---------------------------------------------------------------------------- #

    def wait(self, conditions, by_locator, time=5):
        wait = WebDriverWait(self.driver, time).until(
            conditions(by_locator))
        return wait

    def wait_txt(self, conditions, by_locator, txt, time=5):
        wait_txt = WebDriverWait(self.driver, time).until(
            conditions(by_locator, txt))
        return wait_txt

# ---------------------------------------------------------------------------- #

class BasePage(Templates):

    def __init__(self, driver):
        self.driver = driver

# ---------------------------------------------------------------------------- #
# >---- pytest -vs --alluredir="reports/" Tests/test_...py ----- #
# >-------------------------- allure serve reports --------------------------- #

    def do_allure_scrshot(self, scr_name):
        allure.attach(self.driver.get_screenshot_as_png(
        ), name=scr_name, attachment_type=AttachmentType.PNG)

    def do_get_title(self):
        return self.driver.title
# >--------------------------------------------------------------------------- #

    def do_scroll(self, PIX_VERT):
        self.driver.execute_script(f"window.scrollBy(0, {PIX_VERT});")

    def do_wait_visible(self, by_locator, time=5):
        element = self.wait(self.cond().visible, by_locator, time)
        return bool(element)

    def do_get_attr(self, by_locator, attr):
        element = self.driver.find_element(*by_locator)
        return element.get_attribute(attr)

    def do_get_selector(self, by_locator, value):
        select = Select(self.driver.find_element(*by_locator))
        return select.select_by_value(value)

    def do_wait_visible_text(self, by_locator, time=5):
        element = self.wait(self.cond().visible, by_locator, time)
        return element.text

    def do_wait_all_visible(self, by_locator, time=5):
        elements = self.wait(self.cond().visible_all, by_locator, time)
        return len(elements)

    def do_wait_present(self, by_locator, time=5):
        element = self.wait(self.cond().present, by_locator, time)
        return bool(element)

    def do_wait_txt_present(self, by_locator, txt, time=5):
        element = self.wait_txt(
            self.cond().text_present, by_locator, txt, time)
        return bool(element)

    def do_wait_click(self, by_locator, time=5):
        self.wait(self.cond().clickable, by_locator, time).click()

    def do_wait_clear(self, by_locator, time=5):
        self.wait(self.cond().visible, by_locator, time).clear()

    def do_simple_click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def do_wait_send_keys(self, by_locator, text, time=5):
        self.wait(self.cond().visible, by_locator, time).send_keys(text)


    def do_find_elements_len(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        return len(elements)

    def do_find_element_text(self, by_locator):
        element = self.driver.find_element(*by_locator)
        return element.text

    def do_get_number_from_str(self, by_locator):
        element = self.do_find_element_text(by_locator)
        element_num = ''.join(filter(str.isdigit, element))
        return int(element_num)

    def do_wait_title(self, title, time=5):
        try:
            self.wait(self.cond().title, title, time)
            return self.driver.title
        except Exception:
            return self.driver.title

# ---------------------------------------------------------------------------- #
