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
#                2. Click on "Shop" Link & Scroll 300 pixels                   #
# ---------------------------------------------------------------------------- #
driver.find_element(By.LINK_TEXT, "Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
# ---------------------------------------------------------------------------- #
#            3. Add book "HTML5 WebApp Development" to the cart                #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
# ---------------------------------------------------------------------------- #
#                               4. Go to the Cart                              #
# ---------------------------------------------------------------------------- #
driver.find_element(By.XPATH, "//a[@class='wpmenucart-contents']").click()
# ---------------------------------------------------------------------------- #
#                       5. Click on "PROCEED TO CHECKOUT"                      #
# ---------------------------------------------------------------------------- #
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(@*, 'checkout')]"))).click()
# ---------------------------------------------------------------------------- #
#                       6. Fill out the Billing Ditails                        #
# ---------------------------------------------------------------------------- #
first_name = driver.find_element(By.ID, "billing_first_name")
first_name.send_keys("Bob")

last_name = driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Marley")

email_name = driver.find_element(By.ID, "billing_email")
email_name.send_keys("book@inpwa.com")

phone_name = driver.find_element(By.ID, "billing_phone")
phone_name.send_keys("+12509998877")

country_selector = driver.find_element(By.ID, "select2-chosen-1").click()
country_enter = driver.find_element(By.ID, "s2id_autogen1_search")
country_enter.send_keys("Canada")
driver.find_element(By.CLASS_NAME, "select2-match").click()

address_name = driver.find_element(By.ID, "billing_address_1")
address_name.send_keys("30 Quadra St")

city_name = driver.find_element(By.ID, "billing_city")
city_name.send_keys("Victoria")

province_selector = driver.find_element(
    By.XPATH, "//*[contains(text(), 'Select an option…')]").click()
province_name = driver.find_element(By.CSS_SELECTOR, "#select2-drop input")
province_name.send_keys("British")
driver.find_element(By.CLASS_NAME, "select2-match").click()

postcode_name = driver.find_element(By.ID, "billing_postcode")
postcode_name.send_keys("V8X 4C5")
# ---------------------------------------------------------------------------- #
#                      7. Select "Check Payments" method                       #
# ---------------------------------------------------------------------------- #
driver.execute_script("window.scrollBy(0, 600);")
wait.until(EC.element_to_be_clickable(
    (By.ID, "payment_method_cheque"))).click()
# ---------------------------------------------------------------------------- #
#                         8. Click 'PLACE ORDER' Button                        #
# ---------------------------------------------------------------------------- #
driver.find_element(By.ID, "place_order").click()
# ---------------------------------------------------------------------------- #
#      9. Check if "Thank you..." displays on the page (explicit waiting)      #
# ---------------------------------------------------------------------------- #
confirm_text = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//p[contains(text(), 'Thank you.')]")))
print('9 Step - Text: \"'+confirm_text.text+'\" is visible on the page')
# ---------------------------------------------------------------------------- #
#           10 Check if "Check Payments" is shown as a Payment Method          #
# ---------------------------------------------------------------------------- #
check_pay = wait.until(EC.visibility_of_all_elements_located(
    (By.XPATH, "//*[text()='Check Payments']")))
print('\n10 Step - All '+str(len(check_pay)) +
      ' Payment Methods on the page are set to \"Check Payments\"')
# ---------------------------------------------------------------------------- #
driver.quit()
