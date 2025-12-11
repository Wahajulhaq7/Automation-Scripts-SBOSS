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
    
    print("Locating Password field...")
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.clear()
    password_input.send_keys("Wahajulhaq123@")

    print("Toggling Supervisor switch...")
    supervisor_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='loginAsSupervisor']")))
    supervisor_label.click()

    print("Clicking Login button...")
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-login')]")))
    driver.execute_script("arguments[0].click();", login_btn)
    print("Login clicked. Waiting for dashboard...")

    # --- Dashboard Navigation Phase ---
    print("Locating 'Work Flow'...")
    workflow_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Work Flow')]")))
    workflow_btn.click()
    print("Clicked 'Work Flow'.")

    # --- Service Request Section (New Steps) ---

    # 1. Click 'Service Request' Button
    print("Locating 'Service Request' button...")
    service_req_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Service Request')]")))
    service_req_btn.click()
    print("Clicked 'Service Request'. Waiting 5s...")
    time.sleep(5)

    # 2. Enter SR Name
    print("Entering SR Name...")
    sr_name_input = wait.until(EC.presence_of_element_located((By.ID, "srName")))
    sr_name_input.clear()
    sr_name_input.send_keys("My Test Request")
    print("SR Name entered.")

    # 3. Select RLCO (test department)
    print("Opening RLCO Dropdown...")
    rlco_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select a RLCO')]")))
    rlco_dropdown.click()
    time.sleep(2) # Wait for list to open

    print("Selecting 'test department'...")
    rlco_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'mat-option-text') and contains(text(), 'test department')]")))
    rlco_option.click()
    print("RLCO Selected.")
    time.sleep(2)

    # 4. Select Category (Registration)
    print("Opening Category Dropdown...")
    # Sometimes clicking the dropdown needs a forced JS click if labels overlap
    cat_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select a Category')]")))
    cat_dropdown.click()
    time.sleep(2)

    print("Selecting 'Registration'...")
    cat_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'mat-option-text') and contains(text(), 'Registration')]")))
    cat_option.click()
    print("Category Selected.")
    time.sleep(1)

    # 5. Enter Internal TAT (10)
    print("Entering Internal TAT...")
    internal_tat = wait.until(EC.presence_of_element_located((By.ID, "internalTat")))
    internal_tat.clear()
    internal_tat.send_keys("10")
    print("Internal TAT entered.")

    # 6. Enter Customer TAT (20)
    print("Entering Customer TAT...")
    customer_tat = wait.until(EC.presence_of_element_located((By.ID, "customerTat")))
    customer_tat.clear()
    customer_tat.send_keys("20")
    print("Customer TAT entered.")
    
    # 7. Scroll and Click 'Step 1'
    print("Locating 'Step 1' panel...")
    step1_panel = wait.until(EC.presence_of_element_located((By.XPATH, "//mat-panel-title[contains(text(), 'Step 1')]")))
    
    # Scroll into view (replaces "scroll two times a bit")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", step1_panel)
    time.sleep(2) # Wait for scroll
    
    step1_panel.click()
    print("Clicked 'Step 1'. Waiting for expansion...")
    time.sleep(3) # Wait for animation to open the panel

    # 8. Select Officer (District Health Officer)
    print("Opening Officer Dropdown...")
    # Finding dropdown inside the now expanded panel
    officer_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select a Officer')]")))
    officer_dropdown.click()
    time.sleep(2)

    print("Selecting 'District Health Officer'...")
    officer_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'mat-option-text') and contains(text(), 'District Health Officer')]")))
    officer_option.click()
    print("Officer Selected.")
    time.sleep(1)

    # 9. Enter Turn Around Time (tat0)
    print("Entering TAT for Officer...")
    # Using formcontrolname as it's more stable than dynamic IDs like mat-input-23
    tat0_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='tat0']")))
    tat0_input.clear()
    tat0_input.send_keys("10")
    print("Officer TAT entered.")

    # Final wait to observe
    time.sleep(15)

except TimeoutException:
    print("Error: The page took too long to load a specific element.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Cleanup
    driver.quit()