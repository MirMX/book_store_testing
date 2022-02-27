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
#                          4. Open "HTML 5 Forms" book                         #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//h3[text()='HTML5 Forms']").click()
# ---------------------------------------------------------------------------- #
#                5. Test if Title of the book is "HTML 5 Forms"                #
# ---------------------------------------------------------------------------- #
book_title_exp = "HTML5 Forms"
book_title = driver.find_element(By.XPATH, "//h1[text()='HTML5 Forms']")
print("------ 5 Step (assert) ------")
print("The Title Rusult:", book_title.text,
      "\nExpected Result:", book_title_exp)
print("-----------------------------")
assert book_title.text == book_title_exp
# ---------------------------------------------------------------------------- #
driver.quit()