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

# ---- Departments ----
try:
    # -------------------------Navigate to Application-------------------------
    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[ contains(text(), ' Departments ')  ]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Agriculture Department')] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Distributor Registration License for both Pesticides and Fertilizer')] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),' Registration ')] "))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Apply Now')] "))).click()

except Exception as e:
    print("❌ Navigation failed:", e)
    driver.quit()
    raise SystemExit

# -----------------------------Form-1----------------------------------------------

# ---- Dropdowns ----
dropdowns = [
    ("FERTILIZER", 1),
    ("Karachi", 2),
    ("Hyderabad", 3),
    ("Clifton", 4)
]

for value, index in dropdowns:
    try:
        # Click the dropdown trigger
        dropdown = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"(//div[contains(@class,'mat-mdc-select-value')])[{index}]"
        )))
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()
        time.sleep(0.5)  # allow overlay to render

        # Wait until the option is visible
        option = wait.until(EC.visibility_of_element_located((
            By.XPATH, f"//span[contains(@class,'mdc-list-item__primary-text') and normalize-space()='{value}']"
        )))

        # Click using ActionChains
        actions = ActionChains(driver)
        actions.move_to_element(option).click().perform()

        print(f"✅ Dropdown {index} selected: {value}")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Dropdown {index} selection failed: {e}")

# ---- Fill text fields ----
fields = {
    "//input[@placeholder='Enter First Name']": "John",
    "//input[@placeholder='Enter Last Name']": "Doe",
    "//input[@placeholder=\"Enter Father's Name\"]": "Ali",
    "//input[@placeholder='XXXXX-XXXXXXX-X']": "42401-2788401-7",
    "//input[@placeholder='+92XXXXXXXXXX']": "+923001234567",
    "//input[@placeholder='Enter Email Address']": "test@example.com",
    "//input[@placeholder='XXXXX-X']": "75600-1",
    "//input[@placeholder='Enter Name of Company']": "BenchMatrix",
    "//input[@placeholder='Enter Brand Name']": "FBL",
    "//input[@placeholder='Enter Postal Address']": "House No. 123, Street 4, Karachi"
}

for xpath, value in fields.items():
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(value)
    except Exception as e:
        print(f"❌ Failed to fill field {xpath}: {e}")

# ------------------- Map Field ------------------
try:
    map_field = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//input[@placeholder='Select Location']"
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", map_field)
    driver.execute_script("arguments[0].click();", map_field)
    print("✅ Map field clicked successfully!")
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
    next_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[normalize-space()='Next']]")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", next_btn)
    print("✅ Next button clicked successfully!")
except Exception as e:
    print(f"❌ Failed to click Next button: {e}")


# -------------------------------------------------------

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


# -----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# ---- Assuming driver and wait are already defined ----
# file path to upload
file_path = r"C:\Users\Synergates-PC\Downloads\upload-doc.pdf"

# locate all upload buttons (first 5)
try:
    upload_buttons = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//button[contains(@class,'upload-button')]"
    )))

    for i, button in enumerate(upload_buttons[:13], start=1):  
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


# ------------------------ Submit button ----------------------------
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//button[contains(@class,'button-primary') and .//span[normalize-space(text())='Submit']]").click()
    driver.find_element(By.XPATH, "//button[contains(@class,'swal2-confirm') and normalize-space(text())='Yes']").click()
    print("Submit clicked successfully")
except Exception as e:
    print("Submit not clicked")

   
time.sleep(60)