import time
from tkinter.filedialog import Open
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
driver.get("http://practice.automationtesting.in/")
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

driver.find_element(By.XPATH, "//a[text()='HTML']").click()
time.sleep(5)

html_qty = driver.find_element(By.XPATH, "//ul[@class='product-categories']/li[2]/span")
html_qty.get_attribute("text()")
print(html_qty.text)
x= ''.join(filter(str.isdigit, html_qty.text))
print(int(x))
print(8+int(x))
# ---------------------------------------------------------------------------- #
driver.quit()