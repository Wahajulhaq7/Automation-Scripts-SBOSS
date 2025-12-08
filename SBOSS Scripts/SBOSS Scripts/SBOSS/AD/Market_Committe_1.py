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


# ---- Navigate through options ----
try:
    # -------------------------Navigate to Application-------------------------
    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[ contains(text(), ' Departments ')  ]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Agriculture Department')] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Registration for Market Committee License Retailer Wholesaler Factories')] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),' Registration ')] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Apply Now')] "))).click()

except Exception as e:
    print("❌ Navigation failed:", e)
    driver.quit()
    raise SystemExit

# ---- Dropdown ----
time.sleep(3)
try:
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'mat-mdc-select-value')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    dropdown.click()
    option_xpath = "//span[contains(text(), 'Commission Agents of Grain Market Vegetable and Fruit Markets')]"
    option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", option)
    option.click()
    print("✅ Dropdown option selected!")
except Exception as e:
    print("❌ Dropdown selection failed:", e)

# ---- Fill Input Fields ----
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='+92XXXXXXXXXX']"))).send_keys("3001234567")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-X']"))).send_keys("75820-9")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[3]"))).send_keys("Third Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[4]"))).send_keys("Fourth Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[5]"))).send_keys("Fifth Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[6]"))).send_keys("Sixth Field Data")
    wait.until(EC.visibility_of_element_located((By.ID, "9ac9a72f-92f8-453c-cc84-08ddef6ca134"))).send_keys("Seventh Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-XXXXXXX-X']"))).send_keys("4210112345678")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))).send_keys("Eighth Field Data")
    wait.until(EC.visibility_of_element_located((By.ID, "511457c5-5b90-4df3-cc9f-08ddef6ca134"))).send_keys("Ninth Field Data")
    wait.until(EC.visibility_of_element_located((By.ID, "4f897ea0-dcd2-4295-cca2-08ddef6ca134"))).send_keys("Tenth Field Data")
    print("✅ All input fields filled!")
except Exception as e:
    print("❌ Failed to fill input fields:", e)

# ---- Click Next ----
try:
    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Next']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
    driver.execute_script("arguments[0].click();", next_btn)
    print("✅ Next button clicked!")
except Exception as e:
    print("❌ Next button failed:", e)

# ---- Upload Document (first upload) ----
# file path to upload
file_path = r"C:\Users\Synergates-PC\Downloads\upload-doc.pdf"
file_path = r"C:\Users\Synergates-PC\Downloads\challan1.pdf"

# locate all upload buttons (first 5)
try:
    upload_buttons = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//button[contains(@class,'upload-button')]"
    )))

    for i, button in enumerate(upload_buttons[:1], start=1):  
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            driver.execute_script("arguments[0].click();", button)  # open file dialog

            # Upload file (send keys to input[type='file'] inside dialog)
            # Usually, a hidden input[type='file'] appears after clicking upload
            file_input = wait.until(EC.presence_of_element_located((
                By.XPATH, "//input[@type='file']"
            )))
            file_input.send_keys(file_path)
            time.sleep(1)  # wait for upload

            print(f"✅ Document {i} uploaded successfully!")

        except Exception as e:
            print(f"❌ Upload failed for Document {i}: {e}")

except Exception as e:
    print(f"❌ Failed to locate upload buttons: {e}")


# ---- Click Next ----
try:
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space(text())='Next']]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    driver.execute_script("arguments[0].click();", next_button)
    print("✅ Next button clicked successfully!")
except Exception as e:
    print("❌ Next button click failed:", e)

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
    # Click the date field (not its wrapper)
    date_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='paymentDate']")))
    date_field.click()
    print("Date field clicked")

     # Click date "1" (works for all Angular calendar states)
    date_to_click = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//td[contains(@class,'mat-calendar-body-cell')]//span[normalize-space()='1']"
    )))
    date_to_click.click()

    print("Date selected successfully")

except Exception as e:
    print("Date selection failed:", e)



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
    # driver.find_element(By.XPATH, "//button[contains(@class,'button-primary') and .//span[normalize-space(text())='Submit']]").click()
    # driver.find_element(By.XPATH, "//button[contains(@class,'swal2-confirm') and normalize-space(text())='Yes']").click()
    print("Submit clicked successfully")
except Exception as e:
    print("Submit not clicked")
time.sleep(3)

# -------------------Wait until the submitted application appears on the dashboard -----------------
try:
    # Wait until the submitted application appears on the dashboard
    success_text = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(@class,'rlco-text') and normalize-space(text())='Registration for Market Committee License Retailer Wholesaler Factories']"))
    )
    print("✅ Application submitted successfully and visible on the dashboard.")
except Exception as e:
    print("❌ Application submission not verified:", e)

# ----------------------------Script Ended-------------------------------------
time.sleep(60)