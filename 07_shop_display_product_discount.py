from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
#                   4. Open book "Android Quick Start Guide"                   #
# ---------------------------------------------------------------------------- #
driver.find_element(
    By.XPATH, "//h3[text() ='Android Quick Start Guide']").click()
# ---------------------------------------------------------------------------- #
#                        5. Assert Old Price of the book                       #
# ---------------------------------------------------------------------------- #
old_price_exp = "₹600.00"
old_price = driver.find_element(By.XPATH, "//del/span")
print("--- 5 Step (assert Old Price) ---")
print("The Old Price Rusult:", old_price.text,
      "\nExpected Old Price Result:", old_price_exp)
print("---------------------------------")
assert old_price.text == old_price_exp
# ---------------------------------------------------------------------------- #
#                        6. Assert New Price of the book                       #
# ---------------------------------------------------------------------------- #
new_price_exp = "₹450.00"
new_price = driver.find_element(By.XPATH, "//ins/span")
print("--- 6 Step (assert New Price) ---")
print("The New Price Rusult:", new_price.text,
      "\nExpected New Price Result:", new_price_exp)
print("---------------------------------")
assert new_price.text == new_price_exp
# ---------------------------------------------------------------------------- #
#                     Book Cover Image (Explicit  Waiting)                     #
# ---------------------------------------------------------------------------- #
wait = WebDriverWait(driver, 10).until
ec_click = EC.element_to_be_clickable
# >---------------------- 7. Click on Book cover image ----------------------- #
wait(ec_click((By.CLASS_NAME, "wp-post-image"))).click()
# >---------------------- 8. Close the Book cover image ---------------------- #
wait(ec_click((By.CLASS_NAME, "pp_close"))).click()
# ---------------------------------------------------------------------------- #
driver.quit()
