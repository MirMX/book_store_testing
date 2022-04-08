import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
# ---------------------------------------------------------------------------- #
#                   *   Loading Chrome Profile for testing   *                 #
# ---------------------------------------------------------------------------- #
profile_1 = r"f:\___QA\Chrome_Profiles\Test_Profile_1"
options = Options()
options.add_argument('user-data-dir=' + profile_1)
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
# ---------------------------------------------------------------------------- #
#                                 1. Open Page                                 #
# ---------------------------------------------------------------------------- #
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)
# ---------------------------------------------------------------------------- #
#                             2. Login into account                            #
# ---------------------------------------------------------------------------- #
driver.find_element(By.LINK_TEXT, "My Account").click()
reg_email = driver.find_element(By.ID, "username")
reg_email.send_keys("book@inpwa.com")

reg_pass = driver.find_element(By.ID, "password")
reg_pass.send_keys("S99gn5X")

reg_btn = driver.find_element(By.XPATH, "//input[@name='login']")
reg_btn.click()
# ---------------------------------------------------------------------------- #
#                             3. Click "Shop" Link                             #
# ---------------------------------------------------------------------------- #
driver.find_element(By.LINK_TEXT, "Shop").click()
# ---------------------------------------------------------------------------- #
#                4. Check if Selection set to "Default sorting"                #
# ---------------------------------------------------------------------------- #
sort_selector = driver.find_element(By.XPATH, "//option[@value='menu_order']")
select_value = sort_selector.get_attribute("selected")
print("4 Step - Selection set to \'Default sorting\':", select_value)
assert select_value == "true"
# ---------------------------------------------------------------------------- #
#                       5. Sorting by price: high to low                       #
# ---------------------------------------------------------------------------- #
sort_selector = driver.find_element(By.CSS_SELECTOR, "select.orderby")
select_sorting = Select(sort_selector)
select_high_low = select_sorting.select_by_value("price-desc")
# ---------------------------- 6. Locate selector ---------------------------- #
sort_selector = driver.find_element(By.XPATH, "//option[@value='price-desc']")
select_value = sort_selector.get_attribute("selected")
# ---------- 7. Check if selection set to "Sort by price: high to low" --------- #
print("\n7 Step - Selection set to \'Sort by price: high to low\':", select_value)
assert select_value == "true"
#> time.sleep(2)
driver.quit()
