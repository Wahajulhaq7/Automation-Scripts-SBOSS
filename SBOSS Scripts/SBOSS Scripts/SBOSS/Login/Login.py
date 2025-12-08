from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://customer-demo.business.gos.pk/login")
wait = WebDriverWait(driver, 20)
time.sleep(5)
driver.find_element(By.ID,"cnic").send_keys("42401-2788401-7")
driver.find_element(By.NAME,"password").send_keys("Rashid@139")
driver.find_element(By.ID,"chatbot").click()
time.sleep(30)
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
print("Login Successfully...")
time.sleep(30)