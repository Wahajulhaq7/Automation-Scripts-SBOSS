from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# ---- Setup ----
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://customer-demo.business.gos.pk/login")
wait = WebDriverWait(driver, 30)


# ------ Login -----------
try:
    wait.until(EC.visibility_of_element_located((By.ID, "cnic"))).send_keys("42401-2788401-7")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Rashid@139")
    wait.until(EC.element_to_be_clickable((By.ID, "chatbot"))).click()
    time.sleep(20)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Sign In")]'))).click()
    print("✅ Login successful!")
    time.sleep(5)
except Exception as e:
    print(f"❌ Login failed: {e}")
    driver.quit()
    raise SystemExit


# -------------------------Navigate to Application-------------------------
wait.until(EC.element_to_be_clickable((By.XPATH,"//a[ contains(text(), ' Departments ')  ]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Sindh Employee Social Security Institution')] "))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Registration of Establishment')] "))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),' Registration ')] "))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Apply Now')] "))).click()

# -------------------------Start Application-------------------------
time.sleep(3)
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Enter Name']"))).send_keys("Fareed")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Enter Middle Name']"))).send_keys("Ahmed")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Enter Last Name']"))).send_keys("Fareed Ahmed third")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Enter Father/Husband Name']"))).send_keys("Fareed Ahmed third")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='XXXXX-XXXXXXX-X']"))).send_keys("12345-1234567-8")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='+92XXXXXXXXXX']"))).send_keys("1234567898")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='021-XXXXXXXX']"))).send_keys("021-12345678")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Example@example.com']"))).send_keys("test@gmail.com")

# ----------Drop Down-1--------------------
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[ contains(@class,'mat-mdc-select-value')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[ contains(@class,'mdc-list-item__primary-text') and normalize-space()='Karachi']"))).click()


# ----------Drop Down-2--------------------
wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'mat-mdc-select-value')])[2]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[ contains(@class,'mdc-list-item__primary-text') and normalize-space()='Badin']"))).click()

# ----------Drop Down-3--------------------
wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'mat-mdc-select-value')])[3]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[ contains(@class,'mdc-list-item__primary-text') and normalize-space()='Clifton']"))).click()

# -----------Map ------------
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[ contains(@class,'map-field-wrapper ng-star-inserted')]"))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[ contains(@class,'submit-button mt-2 mb-2 border-12 ng-star-inserted' ) ]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[ contains(., ' Next ')  ]"))).click()

# ----------------second screen-------------------------------
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='First Name']"))).send_keys("Fareed")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Last Name']"))).send_keys("Fareed Ahmed")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='XXXXX-XXXXXXX-X']"))).send_keys("44344-6756756-8")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='+92XXXXXXXXXX']"))).send_keys("3021980743")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Example@example.com']"))).send_keys("test@gmail.com")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[ contains(., ' Next ')  ]"))).click()

# ----------------3rd screen (BUSINESS DETAILS)-------------------------------
try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'mat-mdc-select-value') ] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[ contains(text(),'Other')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[ contains(., ' Next ')  ]"))).click()
except Exception as e:
    print("Failed at 3rd page")
   
time.sleep(2)

# ----------------4th screen  (BRANCH OFFICE DETAIL)-------------------------------
try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'mat-mdc-select-value') ] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[ contains(text(),'No')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[ contains(., ' Next ')  ]"))).click()
except Exception as e:
    print("Failed at 4th page")

time.sleep(2)

# ----------------5th screen (EMPLOYEES' DETAIL)-------------------------------
try:
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@class,'ng-untouched ng-pristine ng-valid ng-star-inserted') ]"))).send_keys("2")
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='No. of Females']"))).send_keys("3")
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Enter No. of Males']"))).send_keys("4")
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[ @placeholder='Enter No. of Females']"))).send_keys("5")
    time.sleep(2)

    # Scroll to Select dropdown
    select_dropdown = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span [ contains(text(),' Are Any Members Employeed? ')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", select_dropdown)
    time.sleep(1)

    # Click Select dropdown
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='mat-mdc-select-value']"))).click()
    print("Select dropdown is clicked")
    time.sleep(2)

    wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//span[@class='mdc-list-item__primary-text' and text()='No']"))).click()
    print("No is clicked")
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @pattern='^[0-9]+$']"))).send_keys("7")
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[ contains(., ' Next ')  ]"))).click()
except Exception as e:
    print("Failed at 5th screen")

# -------------------DOCUMENTS REQUIRED Screen-------------------

try:
    # Upload first document
    first_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    first_input.send_keys("C:\\Users\\syner\\Downloads\\site logo 2.png")
    time.sleep(2)  # wait for upload to complete

    # Upload second document (re-locate the input)
    second_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    second_input.send_keys("C:\\Users\\syner\\Downloads\\upload_doc2.png")
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[ contains(., ' Next ')  ]"))).click()
    print("Documents uploaded")
except Exception as e:
    print("Documents Failed to upload")
# -------------------CONFIRMATION Screen-------------------
try:
    #  Click directorate Select dropdown
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[ @class='mat-mdc-select-value']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[ contains(text(),'Clifton Defence Directorate')]"))).click()
    print("Select dropdown is clicked")
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[ contains(.,' Submit ')]"))).click()

    # Press Enter
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    print("Application submitted ")
except Exception as e:
    print("Application submittion Failed")
# ---------------------------------------------------------------------
time.sleep(40)


