from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
import time
import datetime

# ---- Setup ----
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://customer-demo.business.gos.pk/login")
wait = WebDriverWait(driver, 30)

# ---- Login ----
try:
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.ID, "cnic"))).send_keys("42401-2788401-7")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Rashid@139")
    wait.until(EC.element_to_be_clickable((By.ID, "chatbot"))).click()
    time.sleep(20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()
    print("✅ Login Successfully...")
except TimeoutException:
    print("❌ Login step failed.")
    driver.quit()
    raise SystemExit


# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# ---- Departments ----
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='departments']"))).click()
print("✅ Departments page opened successfully!")



# ---- Navigate through options ----
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Agriculture Department']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Registration for Product License for Fertilizer Micronutrients']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Registration']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply Now')]"))).click()
    print("✅ Apply Now clicked!")
except Exception as e:
    print("❌ Navigation failed:", e)
    driver.quit()
    raise SystemExit


# -----------------------------Form-1----------------------------------------------
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter First Name']"))).send_keys("John")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Last Name']"))).send_keys("Doe")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder=\"Enter Father's Name\"]"))).send_keys("Ali")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-XXXXXXX-X']"))).send_keys("42401-2788401-7")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='+92XXXXXXXXXX']"))).send_keys("+923001234567")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Email']"))).send_keys("test@example.com")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-X']"))).send_keys("75600-1")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Name of Comany']"))).send_keys("Synergates Pvt Ltd")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Brand Name ']"))).send_keys("TEST BRAND")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Postal Address']"))).send_keys("House No. 123, Street 4, Karachi")

# ------------------- Drop Down 1 -------------------
try:
    dropdown_1 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[contains(@class,'mat-mdc-select-value')][1]"
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_1)
    driver.execute_script("arguments[0].click();", dropdown_1)

    option_1 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[contains(@class,'mdc-list-item__primary-text') and normalize-space()='Karachi']"
    )))
    driver.execute_script("arguments[0].click();", option_1)
    print("✅ Dropdown 1 selected: Karachi")
except Exception as e:
    print(f"❌ Dropdown 1 selection failed: {e}")

time.sleep(1)

# ------------------- Drop Down 2 -------------------
try:
    dropdown_2 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//div[contains(@class,'mat-mdc-select-value')])[2]"
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_2)
    driver.execute_script("arguments[0].click();", dropdown_2)

    option_2 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[contains(@class,'mdc-list-item__primary-text') and normalize-space()='Ghotki']"
    )))
    driver.execute_script("arguments[0].click();", option_2)
    print("✅ Dropdown 2 selected: Ghotki")
except Exception as e:
    print(f"❌ Dropdown 2 selection failed: {e}")

time.sleep(1)

# ------------------- Drop Down 3 -------------------
try:
    dropdown_3 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//div[contains(@class,'mat-mdc-select-value')])[3]"
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_3)
    driver.execute_script("arguments[0].click();", dropdown_3)

    option_3 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[contains(@class,'mdc-list-item__primary-text') and normalize-space()='Clifton']"
    )))
    driver.execute_script("arguments[0].click();", option_3)
    print("✅ Dropdown 3 selected: Clifton")
except Exception as e:
    print(f"❌ Dropdown 3 selection failed: {e}")
    
# -------------------Map Field ------------------
try:
    map_field = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//input[@placeholder='Select Location']"
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", map_field)
    driver.execute_script("arguments[0].click();", map_field)
    print("✅ Map field clicked successfully!")

    # If a popup or map appears, you can add extra interaction here
    # e.g., wait for map to load, select location, or close popup if needed

    time.sleep(2)
except Exception as e:
    print(f"❌ Map field click failed: {e}")

# ------------------- Submit Button -------------------
try:
    submit_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[contains(@class,'submit-button') and normalize-space()='Submit']"
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    driver.execute_script("arguments[0].click();", submit_btn)
    print("✅ Submit button clicked successfully!")
except Exception as e:
    print(f"❌ Submit button click failed: {e}")

# ------------------- Next Button -------------------
try:
    # Wait until the actual button containing the span text 'Next' is clickable
    next_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[normalize-space()='Next']]")
    ))

    # Scroll into view and click using JS to avoid overlay or intercept issues
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
    time.sleep(0.5)  # brief pause for safety
    driver.execute_script("arguments[0].click();", next_btn)

    print("✅ Next button clicked successfully!")
except Exception as e:
    print("❌ Failed to click Next button:", e)

# -------------------------------------------------------------------------
# ---- Click "+ Add" button ----
add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='+ Add']")))
driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
driver.execute_script("arguments[0].click();", add_btn)
print("✅ '+ Add' button clicked successfully!")
# -------------------------------Category drop down---------------------------------------
try:
    # ---- Open Dropdown ----
    dropdown_trigger = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[contains(@class,'mat-mdc-select-trigger')]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_trigger)
    time.sleep(0.5)  # brief pause for UI stability
    driver.execute_script("arguments[0].click();", dropdown_trigger)
    print("✅ Dropdown opened successfully!")

    # ---- Select Option: 'Individual/Sole Proprietor' ----
    option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[normalize-space()='Individual/Sole Proprietor']"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", option)
    print("✅ 'Individual/Sole Proprietor' selected successfully!")

except Exception as e:
    print(f"❌ Dropdown selection failed: {e}")


# ---- Enter First Name of Partner ----
first_name_input = wait.until(EC.element_to_be_clickable((By.ID, "2725717d-df10-4252-cd0a-08ddef6ca134Row")))
driver.execute_script("arguments[0].scrollIntoView(true);", first_name_input)
first_name_input.clear()
first_name_input.send_keys("Rashid")
print("✅ Entered First Name of Partner successfully!")
# --------------------------------------------------------------------------------------
# ---- Enter Last Name of Partner ----
last_name_input = wait.until(EC.element_to_be_clickable((By.ID, "ad38925c-5dc9-475b-cd0b-08ddef6ca134Row")))
driver.execute_script("arguments[0].scrollIntoView(true);", last_name_input)
last_name_input.clear()
last_name_input.send_keys("Minhaj")
print("✅ Entered Last Name of Partner successfully!")
# ---- Enter CNIC Number of Partner ----
cnic_input = wait.until(EC.element_to_be_clickable((By.ID, "07f5dc94-43d9-4969-cd0c-08ddef6ca134Row")))
driver.execute_script("arguments[0].scrollIntoView(true);", cnic_input)
cnic_input.clear()
cnic_input.send_keys("42101-1234567-1")
print("✅ Entered CNIC Number successfully!")
# ---- Enter Postal Address ----
postal_address_input = wait.until(EC.element_to_be_clickable((By.ID, "f18c06c7-c788-4fa0-cd0d-08ddef6ca134Row")))
driver.execute_script("arguments[0].scrollIntoView(true);", postal_address_input)
postal_address_input.clear()
postal_address_input.send_keys("123 Main Street, Karachi")
print("✅ Entered Postal Address successfully!")
# ---- Enter Mobile Number ----
mobile_input = wait.until(EC.element_to_be_clickable((By.ID, "0ca75d90-cf8c-419f-cd0e-08ddef6ca134Row")))
driver.execute_script("arguments[0].scrollIntoView(true);", mobile_input)
mobile_input.clear()
mobile_input.send_keys("+923001234567")
print("✅ Entered Mobile Number successfully!")
# ---- Enter Name of Companies ----
company_name_input = wait.until(EC.element_to_be_clickable((By.ID, "059ca730-ede3-4703-cd0f-08ddef6ca134Row")))
driver.execute_script("arguments[0].scrollIntoView(true);", company_name_input)
company_name_input.clear()
company_name_input.send_keys("Waseef Cargo Services")
print("✅ Entered Company Name successfully!")

# -----------------------------Submit button-----------------------------------------
submit_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[.//span[normalize-space()='Submit']]")
))
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit_btn)
driver.execute_script("arguments[0].click();", submit_btn)
print("✅ Submit button clicked successfully!")


# ---------------------------------------------------------------------
try:
    # ---- Click the Next button ----
    next_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[.//span[normalize-space()='Next']]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
    time.sleep(0.5)  # optional short wait for smooth UI rendering
    driver.execute_script("arguments[0].click();", next_btn)
    print("✅ Next button clicked successfully!")

except Exception as e:
    print(f"❌ Failed to click Next button: {e}")



time.sleep(2)
# --------------------------------Document Required screen------------------------------------
# 1) Product technical report
try:
    upload_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[.//span[normalize-space()='Upload']])[1]")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", upload_btn)
    driver.execute_script("arguments[0].click();", upload_btn)
    print("✅ Upload button clicked for 'Product’s Technical Report'")

    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(r"C:\Users\Synergates-PC\Downloads\challan1.pdf")
    print("📤 File uploaded for 'Product’s Technical Report'")

    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'upload-dialog') or contains(@class,'cdk-overlay-pane')]")))
    print("✅ Upload completed for 'Product’s Technical Report'")
except Exception as e:
    print(f"❌ Upload failed for 'Product’s Technical Report': {e}")

# ------------------------------------------------------
# 2) Analytical Report
try:
    upload_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[.//span[normalize-space()='Upload']])[2]")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", upload_btn)
    driver.execute_script("arguments[0].click();", upload_btn)
    print("✅ Upload button clicked for 'Analytical Report'")

    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(r"C:\Users\Synergates-PC\Downloads\challan1.pdf")
    print("📤 File uploaded for 'Analytical Report'")

    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'upload-dialog') or contains(@class,'cdk-overlay-pane')]")))
    print("✅ Upload completed for 'Analytical Report'")
except Exception as e:
    print(f"❌ Upload failed for 'Analytical Report': {e}")


# ------------------------------------------------------
# 3)Recipe Report
try:
    upload_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[.//span[normalize-space()='Upload']])[3]")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", upload_btn)
    driver.execute_script("arguments[0].click();", upload_btn)
    print("✅ Upload button clicked for 'Recipe'")

    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(r"C:\Users\Synergates-PC\Downloads\challan1.pdf")
    print("📤 File uploaded for 'Recipe'")

    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'upload-dialog') or contains(@class,'cdk-overlay-pane')]")))
    print("✅ Upload completed for 'Recipe'")
except Exception as e:
    print(f"❌ Upload failed for 'Recipe': {e}")

# ------------------------------------------------------
# 4)Registration Certificate
try:
    upload_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[.//span[normalize-space()='Upload']])[4]")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", upload_btn)
    driver.execute_script("arguments[0].click();", upload_btn)
    print("✅ Upload button clicked for 'Registration Certificate'")

    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(r"C:\Users\Synergates-PC\Downloads\challan1.pdf")
    print("📤 File uploaded for 'Registration Certificate'")

    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'upload-dialog') or contains(@class,'cdk-overlay-pane')]")))
    print("✅ Upload completed for 'Registration Certificate'")
except Exception as e:  
    print(f"❌ Upload failed for 'Registration Certificate': {e}")



# ---------------------------------------------------------------
try:
    # ---- Click the Next button ----
    next_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[.//span[normalize-space()='Next']]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
    time.sleep(0.5)  # optional short wait for smooth UI rendering
    driver.execute_script("arguments[0].click();", next_btn)
    print("✅ Next button clicked successfully!")

except Exception as e:
    print(f"❌ Failed to click Next button: {e}")


# -------------------------Payment Method---------------------------------
try:
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'approved-action-button')]"))).click()
    print("✅ Download button clicked successfully.")
    time.sleep(15)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'select-manual-payment-btn')]"))).click()
    print("✅ Manual Payment button clicked successfully.")
except Exception as e:
    print("❌ Payment section failed:", e)

# ---- Next Button after Payment ----
try:
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space(text())='Next']]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    driver.execute_script("arguments[0].click();", next_button)
    print("✅ Next button clicked successfully after payment!")
except Exception as e:
    print("❌ Next button after payment failed:", e)

time.sleep(5)

# -------------------- DATE SET --------------------
try:
    date_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='paymentDate']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
    driver.execute_script("arguments[0].removeAttribute('readonly');", date_input)
    date_str = datetime.date.today().strftime("%d-%m-%Y")
    driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input')); arguments[0].dispatchEvent(new Event('change'));", date_input, date_str)
    date_input.send_keys(Keys.TAB)
    print(f"✅ Payment date set to {date_str}")
except Exception as e:
    print("❌ Failed to set payment date:", e)

# -------------------- UPLOAD ATTACHMENT --------------------
try:
    # Click the "Browse" button
    browse_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class,'attachment-link') and normalize-space()='Browse']")
    ))
    driver.execute_script("arguments[0].click();", browse_button)
    print("✅ 'Browse' button clicked successfully!")

    # Locate the hidden file input and upload file
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    driver.execute_script("arguments[0].style.display='block';", file_input)
    file_input.send_keys(r"C:\Users\Synergates-PC\Pictures\3.jpg")
    print("✅ File uploaded successfully (step 1).")

except Exception as e:
    print("❌ File upload failed (step 1):", e)

# ------------------------ Submit button ----------------------------
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//button[contains(@class,'button-primary') and .//span[normalize-space(text())='Submit']]").click()
    driver.find_element(By.XPATH, "//button[contains(@class,'swal2-confirm') and normalize-space(text())='Yes']").click()
    print("Submit clicked successfully")
except Exception as e:
    print("Submit not clicked")
time.sleep(3)

# -------------------Wait until the submitted application appears on the dashboard -----------------
try:
    # Wait until the submitted application appears on the dashboard
    success_text = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(@class,'rlco-text') and normalize-space(text())='Registration for Product License for Fertilizer Micronutrients']"))
    )
    print("✅ Application submitted successfully and visible on the dashboard.")
except Exception as e:
    print("❌ Application submission not verified:", e)

#
time.sleep(30)

