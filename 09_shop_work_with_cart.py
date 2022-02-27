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
#                             2. Click "Shop" Link                             #
# ---------------------------------------------------------------------------- #
driver.find_element(By.LINK_TEXT, "Shop").click()
# ---------------------------------------------------------------------------- #
#                             3. Scroll 300 pixels                             #
# ---------------------------------------------------------------------------- #
driver.execute_script("window.scrollBy(0, 300);")
# ---------------------------------------------------------------------------- #
#              3. Add books "HTML5..." & "JS Data..." to the cart              #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@data-product_id='180']").click()
# ---------------------------------------------------------------------------- #
#                               4. Go to the Cart                              #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[@class='wpmenucart-contents']").click()
# ---------------------------------------------------------------------------- #
#            5. Delete book "HTML5 WebApp Development" from the cart           #
# ---------------------------------------------------------------------------- #
time.sleep(1)
driver.find_element(By.XPATH, "//a[@*='remove' and @*='182']").click()
# ---------------------------------------------------------------------------- #
#                                 6. Click Undo                                #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[text()='Undo?']").click()
# ---------------------------------------------------------------------------- #
#                     7. Set Quantity of "JS Data...“ to 3                     #
# ---------------------------------------------------------------------------- #
book_jsdata = driver.find_element(
    By.XPATH, "//input[contains(@name, '045117')]")
book_jsdata.clear()
book_jsdata.send_keys(3)
# ---------------------------------------------------------------------------- #
#                           8. Click "UPDATE BASKET"                           #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//input[@*='Update Basket']").click()
# ---------------------------------------------------------------------------- #
#        9. Assert Quantity of "JS Data Structures and Algorithm" is 3         #
# ---------------------------------------------------------------------------- #
book_jsdata_value_exp = "3"
book_jsdata = driver.find_element(
    By.XPATH, "//input[contains(@name, '045117')]")
book_jsdata_value = book_jsdata.get_attribute("value")
print("--- 9 Step - assert quantity of \'JS Data Structures and Algorithm\' ---")
print("\nRusult:", book_jsdata_value,
      "\nExpected Result:", book_jsdata_value_exp)
print("------------------------------------------------------------------------")
assert book_jsdata_value == book_jsdata_value_exp
# ---------------------------------------------------------------------------- #
#                          10. Click on "APPLY COUPON"                         #
# ---------------------------------------------------------------------------- #
time.sleep(1)
driver.find_element(By.XPATH, "//input[@*='Apply Coupon']").click()
# ---------------------------------------------------------------------------- #
#        11. Check if message "Please enter a coupon code." is displayed       #
# ---------------------------------------------------------------------------- #
coupon_code_exp = "Please enter a coupon code."
coupon_code = driver.find_element(
    By.XPATH, "//li[text()='Please enter a coupon code.']")
print("--- 11 Step - assert message \'Please enter a coupon code.\'---")
print("\nRusult:", coupon_code.text,
      "\nExpected Result:", coupon_code_exp)
print("------------------------------------------------------------------------")
assert coupon_code.text == coupon_code_exp
# ---------------------------------------------------------------------------- #
driver.quit()
