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
#                             2. Scroll 600 pixels                             #
# ---------------------------------------------------------------------------- #
driver.execute_script("window.scrollBy(0, 600);")
# ---------------------------------------------------------------------------- #
#                          3. Click on "Selenium Ruby"                         #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//h3[text()='Selenium Ruby']").click()
# ---------------------------------------------------------------------------- #
#                             4. Click on "REVIEWS"                            #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[@href = '#tab-reviews']").click()
# ---------------------------------------------------------------------------- #
#                                5. Give 5 Stars                               #
# ---------------------------------------------------------------------------- #
driver.find_element(By.CSS_SELECTOR, "a.star-5").click()
# ---------------------------------------------------------------------------- #
#                  6. Write "Review" with "Nice book!" message                 #
# ---------------------------------------------------------------------------- #
comment_box = driver.find_element(By.ID, "comment")
comment_box.send_keys("Nice book!")
# ---------------------------------------------------------------------------- #
#                                7. Fill "Name"                                #
# ---------------------------------------------------------------------------- #
name_box = driver.find_element(By.ID, "author")
name_box.send_keys("Bob")
# ---------------------------------------------------------------------------- #
#                                8. Fill "Email"                               #
# ---------------------------------------------------------------------------- #
email_box = driver.find_element(By.ID, "email")
email_box.send_keys("book@inpwa.com")
# ---------------------------------------------------------------------------- #
#                           9. Click "SUBMIT" button                           #
# ---------------------------------------------------------------------------- #
time.sleep(3)
submit_btn = driver.find_element(By.ID, "submit")
submit_btn.click()
# ---------------------------------------------------------------------------- #
driver.quit()
