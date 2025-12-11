from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ---- Setup ----
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://officer-demo.business.gos.pk/login")

# Create a wait object
wait = WebDriverWait(driver, 30)

try:
    # --- Login Phase ---
    print("Locating CNIC field...")
    cnic_input = wait.until(EC.presence_of_element_located((By.NAME, "userName")))
    cnic_input.clear()
    cnic_input.send_keys("4220131536637")
    print("CNIC entered.")

    print("Locating Password field...")
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.clear()
    password_input.send_keys("Wahajulhaq123@")
    print("Password entered.")

    print("Toggling Supervisor switch...")
    supervisor_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='loginAsSupervisor']")))
    supervisor_label.click()
    print("Supervisor switch toggled.")

    print("Clicking Login button...")
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-login')]")))
    driver.execute_script("arguments[0].click();", login_btn)
    print("Login clicked (via JS). Waiting for dashboard...")

    # --- Dashboard Navigation Phase ---
    print("Locating 'Work Flow'...")
    workflow_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Work Flow')]")))
    workflow_btn.click()
    print("Clicked 'Work Flow'.")

    #print("Locating 'Hierarchy'...")
    #hierarchy_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Hierarchy')]")))
    #hierarchy_btn.click()
    #print("Clicked 'Hierarchy'.")

    #print("Locating 'Government of Sindh' card...")
    #govt_img = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Government of Sindh']")))
    #govt_img.click()
    #print("Clicked 'Government of Sindh' card.")

    # --- New Steps (Edit, Add, Form) ---

    # # 1. Click Edit Icon (Pencil)
    # print("Locating Edit icon...")
    # edit_icon_path = wait.until(EC.presence_of_element_located((By.XPATH, "//*[local-name()='path' and starts-with(@d, 'M13.1445')]")))
    # driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', {bubbles: true}));", edit_icon_path)
    # print("Clicked Edit icon. Waiting for 5 seconds...")
    # time.sleep(5)  # Added Sleep

    # # 2. Click Add Icon (Plus/Orange)
    # print("Waiting for Add icon...")
    # add_icon_path = wait.until(EC.presence_of_element_located((By.XPATH, "//*[local-name()='path' and starts-with(@d, 'M10 0C4.48')]")))
    # driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', {bubbles: true}));", add_icon_path)
    # print("Clicked Add icon. Waiting 5s for new row to appear...")
    # time.sleep(5)

    # # --- CRITICAL FIX: Target the LAST input fields (the new row) ---

    # # 3. Enter Short Form Department (Last Input)
    # print("Locating LAST Short Form input...")
    # # Get ALL inputs with this name
    # all_short_inputs = driver.find_elements(By.CSS_SELECTOR, "input[formcontrolname='departmentName']")
    # # Select the last one from the list [-1]
    # new_row_short_input = all_short_inputs[-1]
    # 
    # driver.execute_script("arguments[0].scrollIntoView();", new_row_short_input)
    # new_row_short_input.clear()
    # new_row_short_input.send_keys("Test Dept Short")
    # print("Entered Short Form in new row. Waiting 2s...")
    # time.sleep(2)

    # # 4. Enter Full Form Department (Last Input)
    # print("Locating LAST Full Form input...")
    # all_full_inputs = driver.find_elements(By.CSS_SELECTOR, "input[formcontrolname='deptShortName']")
    # new_row_full_input = all_full_inputs[-1]
    # 
    # new_row_full_input.clear()
    # new_row_full_input.send_keys("Test Department Full Name")
    # print("Entered Full Form in new row. Waiting 2s...")
    # time.sleep(2)

    # # 5. Click the Dropdown (Last mat-select)
    # print("Opening LAST Dropdown...")
    # # Find all dropdowns and click the last one
    # all_dropdowns = driver.find_elements(By.TAG_NAME, "mat-select")
    # last_dropdown = all_dropdowns[-1]
    # 
    # driver.execute_script("arguments[0].scrollIntoView();", last_dropdown)
    # last_dropdown.click()
    # print("Dropdown clicked. Waiting for list to open (5s)...")
    # time.sleep(5)

    # # 6. Click the Checkbox (Last Checkbox in the list)
    # print("Locating Checkbox...")
    # # This might open an overlay. We need to find the checkboxes that are currently visible.
    # # Usually, the overlay is appended to the body, so we look for visible checkboxes.
    # all_checkboxes = driver.find_elements(By.TAG_NAME, "mat-checkbox")
    # # We click the last one found (or specific one if you need a specific person)
    # # If "select all" is the first one, you might want all_checkboxes[0] of the overlay, 
    # # but let's try the last one as per your flow or a specific index.
    # # For now, let's click the last available checkbox which is likely the one you want to toggle.
    # target_checkbox = all_checkboxes[-1] 
    # 
    # target_checkbox.click()
    # print("Checkbox selected. Waiting 2s...")
    # time.sleep(2)

    # # Close dropdown (Optional: sometimes clicking the backdrop is needed, but Update usually handles it)
    # # If the dropdown stays open and blocks the Update button, uncomment the line below:
    # # driver.find_element(By.TAG_NAME, 'body').click()

    # # 7. Click Update Button
    # print("Clicking Update...")
    # update_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Update')]")))
    # driver.execute_script("arguments[0].click();", update_btn)
    # print("Clicked Update.")
# --- RLCO Section ---
    
    # 1. Click RLCO
    print("Locating 'RLCO' button...")
    rlco_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'RLCO')]")))
    rlco_btn.click()
    print("Clicked 'RLCO'. Waiting 5s...")
    time.sleep(5)

    # 2. Click Add More
    print("Locating 'Add More' button...")
    add_more_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add More')]")))
    add_more_btn.click()
    print("Clicked 'Add More'. Waiting for modal...")
    time.sleep(2)

    # 3. Select Department Dropdown
    print("Opening 'Select Department' dropdown...")
    # Finds the dropdown by the placeholder text "Select Department" inside it
    dept_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select Department')]")))
    dept_dropdown.click()
    print("Dropdown opened. Waiting for options...")
    time.sleep(2)

    # 4. Select "Health Department" from list
    print("Selecting 'Health Department'...")
    health_dept_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'mat-option-text') and contains(text(), 'Health Department')]")))
    health_dept_option.click()
    print("Selected 'Health Department'.")
    time.sleep(1)

    # 5. Enter RLCO Name
    print("Entering RLCO Name...")
    rlco_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='productName']")))
    rlco_name_input.clear()
    rlco_name_input.send_keys("test department")
    print("RLCO Name entered.")

    # 6. Enter RLCO ID
    print("Entering RLCO ID...")
    rlco_id_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='rlcoId']")))
    rlco_id_input.clear()
    rlco_id_input.send_keys("12345") # You didn't specify an ID number, so I added a placeholder '12345'
    print("RLCO ID entered.")

    # 7. Select Category Dropdown
    print("Opening 'Select Category' dropdown...")
    category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select Category')]")))
    category_dropdown.click()
    print("Category dropdown opened. Waiting for options...")
    time.sleep(2)

    # 8. Click the Toggle (Checkbox) inside the list
    print("Clicking checkbox in category list...")
    # We find the first visible pseudo-checkbox in the opened dropdown list
    # If there are multiple options and you need a specific one, we should target the text next to it.
    # For now, this clicks the checkbox element directly as requested.
    checkbox_toggle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-option mat-pseudo-checkbox")))
    checkbox_toggle.click()
    print("Checkbox clicked.")

# --- NEW: Close the dropdown by clicking the background ---
    print("Clicking background to close dropdown list...")
    driver.find_element(By.TAG_NAME, 'body').click()
    time.sleep(2) # Give it a second to close the list
    # ----------------------------------------------------------
    
# 9. Click 'Add' Button (NEW STEP)
    print("Clicking 'Add' button...")
    # Finds the span with text "Add" inside the button
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Add') and not(contains(text(), 'More'))]")))
    
    # Using JS click to ensure it clicks even if the dropdown list is slightly overlapping
    driver.execute_script("arguments[0].click();", add_btn)
    print("Clicked 'Add' button.")

    # Final wait
    time.sleep(15)

except TimeoutException:
    print("Error: The page took too long to load a specific element.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Cleanup
    driver.quit()