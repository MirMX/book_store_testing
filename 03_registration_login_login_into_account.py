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
#                             2. Go to "My Account"                            #
# ---------------------------------------------------------------------------- #
driver.find_element(By.LINK_TEXT, "My Account").click()
# ---------------------------------------------------------------------------- #
#                                3. Enter email                                #
# ---------------------------------------------------------------------------- #
reg_email = driver.find_element(By.ID, "username")
reg_email.send_keys("book@inpwa.com")
# ---------------------------------------------------------------------------- #
#                               4. Enter password                              #
# ---------------------------------------------------------------------------- #
reg_pass = driver.find_element(By.ID, "password")
reg_pass.send_keys("S99gn5X")
# ---------------------------------------------------------------------------- #
#                          5. Click "Login" button                             #
# ---------------------------------------------------------------------------- #
reg_btn = driver.find_element(By.XPATH, "//input[@name='login']")
reg_btn.click()
# ---------------------------------------------------------------------------- #
#                  6. Check if element "Logout" is on the page                 #
# ---------------------------------------------------------------------------- #
print("------- 6 Step -------")
# >------------------------ Check "Logout" by element ------------------------ #
logout = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']")))
if logout is not None:
    print("Element \"Logout\" is on the page!")
# ---------------------------------------------------------------------------- #
driver.quit()
