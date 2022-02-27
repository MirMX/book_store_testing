import time
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
#                             2. Click "Shop" Link                             #
# ---------------------------------------------------------------------------- #
driver.find_element(By.LINK_TEXT, "Shop").click()
# ---------------------------------------------------------------------------- #
#            3. Add book "HTML5 WebApp Development" to the cart                #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
time.sleep(1)
# ---------------------------------------------------------------------------- #
#                  4. Assert Items amount & Price of the book                  #
# ---------------------------------------------------------------------------- #
cart_item_exp = "1 Item"
cart_item = driver.find_element(By.XPATH, "//span[@class='cartcontents']")

cart_amount_exp = "₹180.00"
cart_amount = driver.find_element(By.XPATH, "//span[@class='amount']")

print("--- 4 Step (assert Items amount & Price) ---")
print("Rusults:\n"
      "The Items amount and price:", cart_item.text, cart_amount.text,
      "\n\nExpected Results:\n"
      "The Items amount and price:", cart_item_exp, cart_amount_exp)
print("--------------------------------------------")
assert (cart_item.text == cart_item_exp)
assert (cart_amount.text == cart_amount_exp)
# ---------------------------------------------------------------------------- #
#                               5. Go to the Cart                              #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[@class='wpmenucart-contents']").click()
# ---------------------------------------------------------------------------- #
# >---------------------------- Declare Variables ---------------------------- #
wait = WebDriverWait(driver, 10).until_not
ec_invisible = EC.invisibility_of_element_located
# ---------------------------------------------------------------------------- #
#              6. Check if Subtotal displays in the Basket Totals              #
# ---------------------------------------------------------------------------- #
subtotal_select = driver.find_element(
    By.XPATH, "//td[@data-title='Subtotal']/span")
subtotal = wait(ec_invisible((By.XPATH, "//td[@data-title='Subtotal']/span")))
print("5 Step - Basket Totals"
      "\n         Subtotal is invisible:", subtotal,
      "\n         Subtotal is", subtotal_select.text)
# ---------------------------------------------------------------------------- #
#              7. Check if Subtotal displays in the Basket Totals              #
# ---------------------------------------------------------------------------- #
total_select = driver.find_element(
    By.XPATH, "//td[@data-title='Total']/strong/span")
total = wait(ec_invisible((By.XPATH, "//td[@data-title='Total']/strong/span")))
print("\n6 Step - Basket Totals"
      "\n         Total is invisible:", total,
      "\n         Total is", total_select.text)
# ---------------------------------------------------------------------------- #
driver.quit()
