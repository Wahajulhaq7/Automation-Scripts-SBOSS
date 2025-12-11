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
driver.get("https://officer-demo.business.gos.pk/login")
wait = WebDriverWait(driver, 30)
