"""
Test case #4
Step 1. Go to “https://practice.cydeo.com/”
Step 2. Click on “Registration Form”
Step 3. Enter only one alphabetic character into first
name input box.
Step 4. Verify that warning message is displayed:
“first name must be more than 2 and less than 64
characters long”
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)
driver.get("https://practice.cydeo.com/")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Registration Form")))
# Step 2: Click on "Registration Form"
registration_form_link = driver.find_element(By.LINK_TEXT, "Registration Form")
registration_form_link.click()

# Step 3: Enter only one alphabetic character into first name input box.
first_name_input = driver.find_element(By.NAME, "firstname")
first_name_input.send_keys("A")
time.sleep(2)  # Just to visually confirm the input during the test run
# Step 4: Verify that warning message is displayed
warning_message = driver.find_element(By.XPATH, "//small[@data-bv-validator='stringLength' and @data-bv-for='firstname']")
assert warning_message.is_displayed(), "Warning message is not displayed"
assert warning_message.text == "first name must be more than 2 and less than 64 characters long", "Warning message text does not match"
driver.quit()