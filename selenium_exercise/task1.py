import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
Test case #1
Step 1. Go to “https://practice-cybertekschool.herokuapp.com”
Step 2. Click on “Registration Form”
Step 3. Enter “wrong_dob” into date of birth input
box.
Step 4. Verify that warning message is displayed:
“The date of birth is not valid”
"""
service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)
driver.get("https://practice.cydeo.com/")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Registration Form")))

# Step 2: Click on "Registration Form"
registration_form_link = driver.find_element(By.LINK_TEXT, "Registration Form")
registration_form_link.click()

# Step 3: Enter "wrong_dob" into date of birth input box
dob_input = driver.find_element(By.NAME, "birthday")
dob_input.send_keys("wrong_dob")

    # Step 4: Verify that warning message is displayed
warning_message = driver.find_element(By.XPATH, "//small[@data-bv-validator='date']")
assert warning_message.is_displayed(), "Warning message is not displayed"
assert warning_message.text == "The date of birth is not valid", "Warning message text does not match"

driver.quit()