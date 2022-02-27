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
#                             2. Go to "My Account"                            #
# ---------------------------------------------------------------------------- #
driver.find_element(By.LINK_TEXT, "My Account").click()
# ---------------------------------------------------------------------------- #
#                                3. Enter email                                #
# ---------------------------------------------------------------------------- #
reg_email = driver.find_element(By.ID, "reg_email")
reg_email.send_keys("book@inpwa.com")
# ---------------------------------------------------------------------------- #
#                               4. Enter password                              #
# ---------------------------------------------------------------------------- #
reg_pass = driver.find_element(By.ID, "reg_password")
reg_pass.send_keys("S99gn5X")
# ---------------------------------------------------------------------------- #
#                          5. Click "Register" button                          #
# ---------------------------------------------------------------------------- #
reg_btn = driver.find_element(By.XPATH, "//input[@name='register']")
reg_btn.click()
# ---------------------------------------------------------------------------- #
driver.quit()
