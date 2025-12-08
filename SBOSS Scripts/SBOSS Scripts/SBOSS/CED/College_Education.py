from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---- Setup ----
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://customer-demo.business.gos.pk/login")
wait = WebDriverWait(driver, 30)

# ------ Login Sequence -----------
try:
    print("1. Entering Credentials...")
    wait.until(EC.visibility_of_element_located((By.ID, "cnic"))).send_keys("42201-3153663-7")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Wahajulhaq123@")

    try:
        print("2. Clicking Chatbot/Captcha checkbox...")
        chatbot_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "chatbot")))
        chatbot_checkbox.click()
        print("⚠️ Please solve the CAPTCHA manually now. You have 20 seconds...")
        time.sleep(20) 
    except Exception as e:
        print(f"Chatbot checkbox issue: {e}")

    print("3. Attempting to Sign In...")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Sign In")]'))).click()
    print("✅ Login successful! Waiting for dashboard...")
    
    # ------ Navigation Sequence -----------
    print("4. Navigating to Departments...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Departments')]"))).click()

    print("5. Selecting College Education Department...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'department-name') and contains(text(), 'College Education Department')]"))).click()

    print("6. Selecting Service: Registration of Privately Managed Colleges...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'rlco-name') and contains(text(), 'Registration of Privately Managed Colleges')]"))).click()

    print("7. Selecting Category: Registration...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'category-name') and contains(text(), 'Registration')]"))).click()

    print("8. Clicking 'Apply Now'...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply Now')]"))).click()

    # ------ Form Filling Part 1 (FIXED) -----------
    print("--- Filling Part 1 ---")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Name of College')]"))).send_keys("Apex Alpha College")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Example@example.com')]"))).send_keys("apex.alpha@example.com")

  # 11. Select Date (Year of Establishment)
    print("11. Selecting Year of Establishment (Date)...")
    # Click the input to open calendar
    date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Year of Establishment')]")))
    date_input.click()
    
    # Click the specific date '9' inside the calendar
    date_cell = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='9']")))
    date_cell.click()

    # --- FIX STARTS HERE ---
    # Force close the calendar overlay immediately
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(1) # Small pause to let the calendar animation finish
    # --- FIX ENDS HERE ---

    # ---- Dropdowns (Angular Material) ----
    print("12. Selecting Gender: Male...")
    # Find all Select dropdowns
    selects = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "mat-select")))
    
    # --- FIX: Use JavaScript click to bypass "Click Intercepted" error ---
    driver.execute_script("arguments[0].click();", selects[0])
    
    # Wait for and click the 'Male' option
    male_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Male')]")))
    male_option.click()
    time.sleep(1) # Short pause for animation

    print("13. Selecting Degree Level...")
    # Click the SECOND dropdown
    # We use JS click here too, just to be safe
    driver.execute_script("arguments[0].click();", selects[1])
    
    # Wait for and click 'Degree Level' option
    degree_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Degree Level')]")))
    degree_option.click()
    time.sleep(1)

    print("14. Selecting Program: 2 Years (ADA)...")
    # Click the THIRD dropdown
    driver.execute_script("arguments[0].click();", selects[2])
    
    # Wait for and click '2 Years (ADA)' option
    program_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '2 Years (ADA)')]")))
    program_option.click()
    
    # Since this is a multi-select (checkbox), we might need to close the dropdown manually
    # We press ESCAPE to close the overlay
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # ------ Form Filling Part 2 -----------
    print("--- Filling Part 2 ---")
    
    # Scroll down slightly
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)

    # 15. Enter Individual or Organization
    print("15. Entering Owner Type...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Individual or Organization')]"))).send_keys("Individual")

    # 16. Enter Owner Name
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Owner/Organization Name')]"))).send_keys("Ahmed Ali")

    # 17. Enter Mobile Number (Owner)
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@placeholder, '+92XXXXXXXXXX')])[1]"))).send_keys("3001234567")

    # 18. Enter Principal Name
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Principal Name')]"))).send_keys("Dr. Sarah Khan")

    # 19. Enter Mobile Number (Principal)
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@placeholder, '+92XXXXXXXXXX')])[2]"))).send_keys("3009876543")

    # 20. Enter Address
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Address')]"))).send_keys("Plot 123, Block A, Main Road")

    # Scroll again for Location Dropdowns
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)

    # Re-fetch selects
    selects = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "mat-select")))

    # 21. Select Division: Hyderabad (Index 3) - JS Click
    print("21. Selecting Division...")
    driver.execute_script("arguments[0].click();", selects[3])
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Hyderabad')]"))).click()
    time.sleep(1) 

    # 22. Select District: Badin (Index 4) - JS Click
    print("22. Selecting District...")
    driver.execute_script("arguments[0].click();", selects[4])
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Badin')]"))).click()
    time.sleep(1)

    # 23. Select Tehsil: Khoski (Index 5) - JS Click
    print("23. Selecting Tehsil...")
    driver.execute_script("arguments[0].click();", selects[5])
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Khoski')]"))).click()
    time.sleep(0.5)

    # 24. Handle Map/Location
    print("24. Setting Location on Map...")
    location_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Location of the Institution')]")))
    # Use JS click here too just to be safe
    driver.execute_script("arguments[0].click();", location_input)

    print("    > Clicking Map Submit button...")
    map_submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))
    map_submit_btn.click()
    
    # 25. Final Form Submit
    print("25. Clicking Final Submit...")
    final_submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit') and contains(@class, 'submit-button')]")))
    # final_submit.click() # Uncomment this line when you are ready to actually submit the form
    
    print("✅ All fields filled successfully!")
    time.sleep(20)

except Exception as e:
    print(f"❌ Process failed: {e}")
    driver.quit()
    raise SystemExit