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

    wait.until( EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(), 'Departments')]"))).click()



    print("5. Selecting College Education Department...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'department-name') and contains(text(), 'College Education Department')]"))).click()



    print("6. Selecting Service: Registration of Privately Managed Colleges...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'rlco-name') and contains(text(), 'Registration of Privately Managed Colleges')]"))).click()



    print("7. Selecting Category: Registration...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'category-name') and contains(text(), 'Registration')]"))).click()



    print("8. Clicking 'Apply Now'...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply Now')]"))).click()



    # ------ Form Filling Part 1 -----------

    print("--- Filling Part 1 ---")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Name of College')]"))).send_keys("Apex Alpha College")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Example@example.com')]"))).send_keys("apex.alpha@example.com")



    # 11. Select Date (Year of Establishment)

    print("11. Selecting Year of Establishment (Date)...")

    date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Year of Establishment')]")))

    date_input.click()

    

    # Click the specific date '9' inside the calendar

    date_cell = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='9']")))

    date_cell.click()



    # --- CRITICAL FIX: Close the Calendar overlay ---

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    time.sleep(1) 



    print("12. Selecting Dropdowns...")



    # We locate all visible dropdown triggers (the actual clickable box)

    dropdown_triggers = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".mat-mdc-select-trigger")))

    

    # --- Dropdown 1: Select "Male" ---

    print("   > Clicking Gender Dropdown...")

    driver.execute_script("arguments[0].click();", dropdown_triggers[0])

    

    male_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Male')]")))

    driver.execute_script("arguments[0].click();", male_option)

    time.sleep(1)



    # --- Dropdown 2: Select "Degree Level" ---

    print("   > Clicking Degree Level Dropdown...")

    driver.execute_script("arguments[0].click();", dropdown_triggers[1])

    

    degree_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Degree Level')]")))

    driver.execute_script("arguments[0].click();", degree_option)

    time.sleep(1)



    # --- Dropdown 3: Select "2 Years (ADA)" ---

    print("   > Clicking Program Dropdown (Multi-select)...")

    

    # This XPath finds the trigger specifically inside the multi-select dropdown

    program_dropdown_trigger = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@multiple]//div[contains(@class, 'mat-mdc-select-trigger')]")))

    driver.execute_script("arguments[0].click();", program_dropdown_trigger)

    

    # Select '2 Years (ADA)'

    program_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '2 Years (ADA)')]")))

    driver.execute_script("arguments[0].click();", program_option)



    # Press Escape to close the dropdown list (Critical for multi-selects)

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()



    print("✅ Dropdowns selected successfully!")

    

    # ------ Form Filling Part 2 -----------

    print("--- Filling Part 2 ---")

    

    # Scroll down slightly to bring new fields into view

    driver.execute_script("window.scrollBy(0, 400);")

    time.sleep(1)



    # 13. Enter Individual or Organization

    print("13. Entering Owner Type...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Individual or Organization')]"))).send_keys("Individual")



    # 14. Enter Owner Name

    print("14. Entering Owner Name...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Owner/Organization Name')]"))).send_keys("Ahmed Ali")



    # 15. Enter Mobile Number (Owner)

    print("15. Entering Owner Mobile...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@placeholder, '+92XXXXXXXXXX')])[1]"))).send_keys("3001234567")



    # 16. Enter Principal Name

    print("16. Entering Principal Name...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Principal Name')]"))).send_keys("Dr. Sarah Khan")



    # 17. Enter Mobile Number (Principal)

    print("17. Entering Principal Mobile...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@placeholder, '+92XXXXXXXXXX')])[2]"))).send_keys("3009876543")



    # Scroll again for Address

    driver.execute_script("window.scrollBy(0, 200);")

    time.sleep(0.5)



    # 18. Enter Address

    print("18. Entering Address...")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Enter Address')]"))).send_keys("Plot 123, Block A, Main Road")



    # ------ Form Filling Part 3 (Location) -----------

    print("--- Filling Part 3 (Location) ---")



    # Scroll to reveal location dropdowns

    driver.execute_script("window.scrollBy(0, 300);")

    time.sleep(1)



    # --- Dropdown 4: Division -> Hyderabad ---

    print("19. Selecting Division: Hyderabad...")

    # Re-fetch the list of triggers freshly

    triggers = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".mat-mdc-select-trigger")))

    # Division is usually the 4th visible trigger (Index 3)

    driver.execute_script("arguments[0].click();", triggers[3])

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Hyderabad')]"))).click()

    time.sleep(1)



    # --- Dropdown 5: District -> Badin ---

    print("20. Selecting District: Badin...")

    triggers = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".mat-mdc-select-trigger")))

    driver.execute_script("arguments[0].click();", triggers[4])

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Badin')]"))).click()

    time.sleep(1)



    # --- Dropdown 6: Tehsil -> Badin ---

    print("21. Selecting Tehsil: Badin...")

    triggers = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".mat-mdc-select-trigger")))

    driver.execute_script("arguments[0].click();", triggers[5])

    tehsil_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(), 'Badin')]")))

    driver.execute_script("arguments[0].click();", tehsil_option)

    

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()



    # --- Map Section ---

    print("22. Clicking Map Field...")

    map_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Location of the Institution')]")))

    driver.execute_script("arguments[0].click();", map_input)

    

    print("23. Clicking Submit Button (Map)...")

    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'submit-button') and contains(., 'Submit')]")))

    driver.execute_script("arguments[0].click();", submit_btn)



    # ------ New Steps Added Below (Next, Area, Owned, Amenity) -----------

    print("--- Proceeding to Next Section ---")



    # 24. Click 'Next'
    print("24. Clicking 'Next' button...")

    next_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button-primary')]//span[contains(normalize-space(), 'Next')]")))
    driver.execute_script("arguments[0].click();", next_btn)


    

    # Wait for the next section to load

    time.sleep(2)

   

    # 25. Enter Area of Plot

    print("25. Entering Area of Plot...")

    area_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Area of the Plot in Square Yards')]")))

    area_input.send_keys("500")



   # 26. Select Ownership: Owned
    print("26. Selecting Ownership Status: Owned...")
    
    # FIX: Find the dropdown that is physically located AFTER the 'Area of the Plot' input
    # This ignores hidden dropdowns from previous screens
    owned_dropdown_trigger = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@placeholder, 'Area of the Plot')]/following::mat-select//div[contains(@class,'mat-mdc-select-trigger')])[1]")))
    driver.execute_script("arguments[0].click();", owned_dropdown_trigger)
    
    owned_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Owned')]")))
    driver.execute_script("arguments[0].click();", owned_option)
    time.sleep(0.5)

    # 27. Select Plot Type: Amenity
    print("27. Selecting Plot Type: Amenity...")
    
    # FIX: Find the SECOND dropdown after the 'Area of the Plot' input
    amenity_dropdown_trigger = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@placeholder, 'Area of the Plot')]/following::mat-select//div[contains(@class,'mat-mdc-select-trigger')])[2]")))
    driver.execute_script("arguments[0].click();", amenity_dropdown_trigger)
    
    amenity_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Amenity')]")))
    driver.execute_script("arguments[0].click();", amenity_option)



    print("✅ All steps completed successfully!")

    time.sleep(10)



except Exception as e:

    print(f"❌ Process failed: {e}")

    driver.quit()

    raise SystemExit