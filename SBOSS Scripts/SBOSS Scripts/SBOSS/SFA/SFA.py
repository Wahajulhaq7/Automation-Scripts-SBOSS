from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://customer-demo.business.gos.pk/login")
wait = WebDriverWait(driver, 30)

# ---- Login ----
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.ID, "cnic"))).send_keys("42401-2788401-7")
wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Rashid@139")
wait.until(EC.element_to_be_clickable((By.ID, "chatbot"))).click()
time.sleep(20)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()
print("✅ Login Successfully...")

# ---- Departments ----
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='departments']"))).click()
print("✅ Departments page opened successfully!")

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Agriculture Department']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Registration for Market Committee License Retailer Wholesaler Factories']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Registration']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Apply Now']"))).click()

# ---- Form Fields ----
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))).send_keys("Rashid Minhaj")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='XXXXX-XXXXXXX-X']"))).send_keys("42101-1234567-1")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='+92XXXXXXXXXX']"))).send_keys("+923021980743")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Name of Food Business']"))).send_keys("Al-Madina Foods")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Nature of Business']"))).send_keys("Food Manufacturing")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Owner Name']"))).send_keys("Rashid Minhaj")

# ---------Dropdown 1----------
time.sleep(2)
dropdown = wait.until(EC.element_to_be_clickable((
    By.XPATH, "(//div[contains(@class,'mat-mdc-select-value')])[1]"
)))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
dropdown.click()

option = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//span[contains(text(), 'A-Premises Carrying Out Business of Margarine Banaspati Fat Spreads')]"
)))
driver.execute_script("arguments[0].click();", option)
print("✅ Dropdown 1 selected successfully")

# ---------Dropdown 2----------
# ---------Dropdown 2----------
# Locate the second dropdown using its position instead of ID
dropdown_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'mat-mdc-select-value')])[2]")))

# Scroll and click the dropdown
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_2)
driver.execute_script("arguments[0].click();", dropdown_2)

# Wait for the option to appear and click it
option_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'A-I(Mega Mart/Wholesale Dealer/Warehouses/Distributor)')]")))
driver.execute_script("arguments[0].click();", option_2)
print("✅ Dropdown 2 selected successfully")

# ---- Postal Address ----
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Postal Address']"))).send_keys("123 Main Street, Karachi")

# ---------Dropdown 3----------
# ---------Dropdown 3----------
# Locate the third dropdown (position-based, more reliable)
dropdown_3 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'mat-mdc-select-value')])[3]")))

# Scroll and click the dropdown
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_3)
driver.execute_script("arguments[0].click();", dropdown_3)

# Wait for the option and click it
option_3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Hyderabad']")))
driver.execute_script("arguments[0].click();", option_3)
print("✅ Dropdown 3 selected successfully")

# ---------Dropdown 4----------
dropdown_4 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'mat-mdc-select-value')])[4]")))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_4)
driver.execute_script("arguments[0].click();", dropdown_4)

option_4 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Dadu']")))
driver.execute_script("arguments[0].click();", option_4)
print("✅ Dropdown 4 selected successfully")

# ---------Dropdown 5----------
dropdown_5 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'mat-mdc-select-value')])[5]")))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_5)
driver.execute_script("arguments[0].click();", dropdown_5)

option_5 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Khairpur Nathan Shah']")))
driver.execute_script("arguments[0].click();", option_5)
print("✅ Dropdown 5 selected successfully")

# ---- Map and Submit ----
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'map-field-wrapper')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()
print("✅ Form submitted successfully!")

time.sleep(10)

