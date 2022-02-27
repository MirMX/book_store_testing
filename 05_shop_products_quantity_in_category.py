import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
#                            4. Go to HTML category                            #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[text()='HTML']").click()
time.sleep(1)
# ---------------------------------------------------------------------------- #
#                    5. Check if Quantity of products is 3                     #
# ---------------------------------------------------------------------------- #
html_qty_int_exp = 3  # > Expected Quantity
# >---- 1. Find The Quantity of Products by presented amount on the page ----- #
qty = driver.find_elements(By.XPATH, "//li[contains(@class, 'post-')]")
# >-------- 2. The Quantity of by shown amount in PRODUCT CATEGORIES --------- #
html_qty = driver.find_element(
    By.XPATH, "//ul[@class='product-categories']/li[2]/span")
html_qty_int = ''.join(filter(str.isdigit, html_qty.text))
print("------ 5 Step (assert Quantity) ------")
print("1. The Quantity of Products by presented amount on the page:", len(qty),
      "\n2. The Quantity of by shown amount in PRODUCT CATEGORIES:", html_qty_int,
      "\nExpected Result:", html_qty_int_exp)
print("--------------------------------------")
# ---------------------------------------------------------------------------- #
assert (len(qty) and int(html_qty_int)) == 3
driver.quit()
