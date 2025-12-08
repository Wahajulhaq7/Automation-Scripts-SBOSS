# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import datetime
# # ---- Setup ----
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://customer-demo.business.gos.pk/login")
# wait = WebDriverWait(driver, 30)

# # ---- Login ----
# time.sleep(5)
# wait.until(EC.visibility_of_element_located((By.ID, "cnic"))).send_keys("42401-2788401-7")
# wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Rashid@139")
# wait.until(EC.element_to_be_clickable((By.ID, "chatbot"))).click()
# time.sleep(20)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()
# print("✅ Login Successfully...")

# # ---- Departments ----
# wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='departments']"))).click()
# print("✅ Departments page opened successfully!")

# # ---- Navigate through options ----
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Agriculture Department']"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Registration for Market Committee License Retailer Wholesaler Factories']"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Registration']"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply Now')]"))).click()
# print("✅ Apply Now clicked!")

# # ---- Dropdown ----
# time.sleep(3)  # small buffer
# dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'mat-mdc-select-value')]")))
# driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
# time.sleep(1)
# dropdown.click()

# option_xpath = "//span[contains(text(), 'Commission Agents of Grain Market Vegetable and Fruit Markets')]"
# option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
# driver.execute_script("arguments[0].scrollIntoView(true);", option)
# option.click()
# print("✅ Dropdown option selected!")

# # ---- Fill Input Fields ----
# wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='+92XXXXXXXXXX']"))).send_keys("+923001234567")
# wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-X']"))).send_keys("75820-9")
# wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[3]"))).send_keys("Third Field Data")
# wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[4]"))).send_keys("Fourth Field Data")
# wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[5]"))).send_keys("Fifth Field Data")
# wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[6]"))).send_keys("Sixth Field Data")
# wait.until(EC.visibility_of_element_located((By.ID, "9ac9a72f-92f8-453c-cc84-08ddef6ca134"))).send_keys("Seventh Field Data")
# wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-XXXXXXX-X']"))).send_keys("42101-1234567-8")
# wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))).send_keys("Eighth Field Data")
# wait.until(EC.visibility_of_element_located((By.ID, "511457c5-5b90-4df3-cc9f-08ddef6ca134"))).send_keys("Ninth Field Data")
# wait.until(EC.visibility_of_element_located((By.ID, "4f897ea0-dcd2-4295-cca2-08ddef6ca134"))).send_keys("Tenth Field Data")
# print("✅ All input fields filled!")

# # ---- Click Next ----
# next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Next']")))
# driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
# next_btn.click()
# print("✅ Next button clicked!")

# # ---- Upload Document ----
# # Locate the hidden input[type='file'] element
# # ---- Upload Document ----
# # Wait for the hidden input[type='file'] element
# file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

# # Make it visible if it's hidden
# driver.execute_script("arguments[0].style.display='block';", file_input)

# # Send the file path to upload
# file_input.send_keys(r"C:\Users\Synergates-PC\Downloads\e7dd3ffa-671a-40f2-224d-08de1391575e.pdf")
# print("✅ File uploaded successfully!")

# # ------------------------------------------------------------
# # ---- Click Next Button ----
# next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space(text())='Next']]")))
# driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
# next_button.click()
# print("✅ Next button clicked successfully!")


# # -------------------------Payment Method started---------------------------------
# #wait for chalan to appear on UI
# time.sleep(5)
# # click on donwload button
# # ---- Click Download button ----
# wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'approved-action-button')]"))).click()
# print("✅ Download button clicked successfully.")
# # wait for challan number to be entered
# time.sleep(15)
# # ---- Click Manual Payment button ----
# wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'select-manual-payment-btn')]"))).click()
# print("✅ Manual Payment button clicked successfully.")



# # ---- Click Next Button ----
# next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space(text())='Next']]")))
# driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
# next_button.click()
# print("✅ Next button clicked successfully!")

# # input challan number
# # ---- Enter Reference Number ----
# time.sleep(5)

# # --------------------Date--------------------
# # ---- Select Payment Date ----
# # ---- Select Payment Date from Calendar ----
# payment_date_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='paymentDate']")))
# payment_date_field.click()  # open the calendar

# # ----------------------------------------Date----------------------------------------------------------
# # Get today's day number dynamically (e.g., "30")
# date_value = str(datetime.datetime.now().day)

# try:
#     # Step 1: Click on the date input to open calendar popup
#     date_input = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//input[@formcontrolname='paymentDate']")))
#     driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
#     driver.execute_script("arguments[0].click();", date_input)
#     print("✅ Calendar popup opened successfully.")

#     # Step 2: Wait until the calendar body is visible
#     wait.until(EC.visibility_of_element_located(
#         (By.XPATH, "//table[contains(@class,'mat-calendar-body')]")))
#     time.sleep(1)  # brief pause for animation

#     # Step 3: Select today's date dynamically
#     date_cell = wait.until(EC.element_to_be_clickable((
#         By.XPATH,
#         f"//span[contains(@class,'mat-calendar-body-cell-content') and normalize-space(text())='{date_value}']"
#     )))
#     driver.execute_script("arguments[0].click();", date_cell)
#     print(f"✅ Payment Date ({date_value}) selected successfully.")

#     # Step 4: Wait for overlay/backdrop to disappear after date selection
#     wait.until(EC.invisibility_of_element_located(
#         (By.XPATH, "//div[contains(@class,'cdk-overlay-backdrop') and contains(@class,'cdk-overlay-backdrop-showing')]")))
#     time.sleep(0.5)
#     print("✅ Calendar overlay closed successfully, safe to continue.")

# except Exception as e:
#     print("❌ Failed to select payment date:", e)
# # --------------------------------------------------------
# # ---- Upload Attachment ----
# # Click on "Browse" to open the file upload dialog
# browse_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'attachment-link') and text()='Browse']")))
# browse_button.click()

# # Use JavaScript to make the hidden file input visible (if applicable)
# file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
# driver.execute_script("arguments[0].style.display = 'block';", file_input)

# # Send the file path to upload
# file_input.send_keys(r"C:\Users\Synergates-PC\Pictures\3.jpg")
# print("✅ Document uploaded successfully.")


# # ---- Click Submit Button ----
# submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'button-primary') and .//span[text()=' Submit ']]")))
# submit_button.click()
# print("✅ Submit button clicked successfully.")


# # ---- Click Alert "Yes" Button ----
# yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'swal2-confirm') and text()='Yes']")))
# yes_button.click()
# print("✅ 'Yes' confirmation button clicked successfully.")


# # wait for screen to view
# time.sleep(60)


# # --------------------------------------------------------------------------------------------------
# # Scripts ended
# # --------------------------------------------------------------------------------------------------

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

# ---- Departments ----
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='departments']"))).click()
print("✅ Departments page opened successfully!")

# ---- Navigate through options ----
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Agriculture Department']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Registration for Market Committee License Retailer Wholesaler Factories']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Registration']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply Now')]"))).click()
    print("✅ Apply Now clicked!")
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
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='+92XXXXXXXXXX']"))).send_keys("+923001234567")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-X']"))).send_keys("75820-9")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[3]"))).send_keys("Third Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[4]"))).send_keys("Fourth Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[5]"))).send_keys("Fifth Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[6]"))).send_keys("Sixth Field Data")
    wait.until(EC.visibility_of_element_located((By.ID, "9ac9a72f-92f8-453c-cc84-08ddef6ca134"))).send_keys("Seventh Field Data")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-XXXXXXX-X']"))).send_keys("42101-1234567-8")
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
try:
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    # make visible and set path
    driver.execute_script("arguments[0].style.display='block';", file_input)
    file_input.send_keys(r"C:\Users\Synergates-PC\Downloads\e7dd3ffa-671a-40f2-224d-08de1391575e.pdf")
    print("✅ File uploaded successfully (step 1).")
except Exception as e:
    print("❌ File upload failed (step 1):", e)

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

time.sleep(5)  # wait for challan/reference area to appear

# -------------------- DATE: set value robustly (fix for malformed values) --------------------
try:
    # locate the input (presence -> element may be in DOM but not visible)
    date_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='paymentDate']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
    time.sleep(0.5)

    # Determine placeholder (if available) to guess format
    placeholder = date_input.get_attribute("placeholder") or ""
    formats_to_try = []

    # heuristics: placeholder mention
    if "dd" in placeholder.lower() or "mm" in placeholder.lower() or "yyyy" in placeholder.lower():
        # prefer day-month-year if placeholder suggests it
        formats_to_try = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d"]
    else:
        # common formats to attempt
        formats_to_try = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%d-%m-%y"]

    today_dt = datetime.date.today()
    set_success = False
    last_error = None

    for fmt in formats_to_try:
        try:
            date_str = today_dt.strftime(fmt)
            # remove readonly if present, then set value via JS and dispatch events
            driver.execute_script("arguments[0].removeAttribute('readonly');", date_input)
            driver.execute_script(
                """
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                """,
                date_input, date_str
            )
            # blur to trigger any validation/close logic
            driver.execute_script("arguments[0].blur();", date_input)
            time.sleep(0.7)

            # some UIs require tab to confirm
            date_input.send_keys(Keys.TAB)
            time.sleep(0.7)

            # wait briefly for potential calendar to close (if it had opened)
            try:
                wait.until(EC.invisibility_of_element_located((By.XPATH, "//mat-calendar")), timeout=2)
            except Exception:
                # ignore, we'll force-close below if needed
                pass

            # verify the value is accepted by checking the input's value attribute
            current_val = date_input.get_attribute("value") or ""
            if current_val.strip() != "":
                print(f"✅ Payment date set using format '{fmt}' -> '{current_val}'")
                set_success = True
                break
            else:
                last_error = f"value remained empty after trying {fmt}"
        except Exception as inner_e:
            last_error = str(inner_e)
            # try next format
            continue

    if not set_success:
        # fallback: try ISO yyyy-mm-dd
        try:
            iso_str = today_dt.strftime("%Y-%m-%d")
            driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input')); arguments[0].dispatchEvent(new Event('change'));", date_input, iso_str)
            driver.execute_script("arguments[0].blur();", date_input)
            date_input.send_keys(Keys.TAB)
            time.sleep(0.5)
            print(f"⚠️ Fallback set to {iso_str}, current value: '{date_input.get_attribute('value')}'")
        except Exception as e:
            print("❌ Could not set payment date (fallback failed):", e)

    # Force-close overlays if any remain (safe operations)
    try:
        # press ESC a couple times
        for _ in range(2):
            date_input.send_keys(Keys.ESCAPE)
            time.sleep(0.3)
        # remove common overlay elements if still blocking
        driver.execute_script("""
            document.querySelectorAll('.cdk-overlay-backdrop, .cdk-overlay-container, .mat-calendar').forEach(function(el){
                try{ el.style.display='none'; }catch(e){}
            });
        """)
        time.sleep(0.3)
    except Exception:
        pass

except Exception as e:
    print("❌ Failed to set payment date:", e)

# -------------------- UPLOAD ATTACHMENT (handle modal not closing) --------------------
# ---- Upload Attachment (final document upload fix) ----
try:
    # Click "Browse" link to open upload modal
    browse_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class,'attachment-link') and normalize-space()='Browse']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", browse_button)
    driver.execute_script("arguments[0].click();", browse_button)
    print("📂 Browse clicked, waiting for file input...")

    # Wait until file input becomes available in DOM
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

    # Make it visible for Selenium
    driver.execute_script("""
        arguments[0].style.display = 'block';
        arguments[0].style.visibility = 'visible';
        arguments[0].style.opacity = 1;
    """, file_input)

    # Send file path
    file_path = r"C:\Users\Synergates-PC\Pictures\3.jpg"
    file_input.send_keys(file_path)
    print(f"✅ File selected successfully: {file_path}")

    # Wait for upload confirmation
    time.sleep(2)
    print("⏳ Waiting for upload modal to react...")

    # --- Close upload popup safely ---
    try:
        close_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[normalize-space()='Upload' or normalize-space()='Attach' or normalize-space()='Close' or normalize-space()='Done' or .//mat-icon[text()='close']]"
        )))
        driver.execute_script("arguments[0].click();", close_btn)
        print("✅ Document popup closed successfully.")
    except Exception:
        # Fallback: manually remove overlay if still open
        from selenium.webdriver.common.keys import Keys
        driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        driver.execute_script("""
            document.querySelectorAll('.cdk-overlay-container, .mat-dialog-container, .cdk-overlay-backdrop')
            .forEach(el => el.remove());
        """)
        print("⚠️ No Close/Upload/Attach button found — modal closed manually.")

    time.sleep(2)

except Exception as e:
    print("❌ Final document upload failed:", e)

# ---- Submit ----
try:
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'button-primary') and .//span[text()=' Submit ']]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    try:
        driver.execute_script("arguments[0].click();", submit_button)
    except ElementClickInterceptedException:
        # try to remove overlays and retry
        driver.execute_script("document.querySelectorAll('.cdk-overlay-backdrop').forEach(e=>e.remove());")
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", submit_button)
    print("✅ Submit button clicked successfully.")
    yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'swal2-confirm') and normalize-space(text())='Yes']")))
    driver.execute_script("arguments[0].click();", yes_button)
    print("✅ 'Yes' confirmation button clicked successfully.")
except Exception as e:
    print("❌ Submit process failed:", e)

time.sleep(50)
print("🎯 Script finished, closing browser.")

