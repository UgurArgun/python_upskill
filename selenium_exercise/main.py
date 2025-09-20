import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)

driver.get('https://automationstepbystep.com/online-courses/')
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "s")))
input_element = driver.find_element(By.CLASS_NAME, "s")
input_element.send_keys('robot framework' + Keys.ENTER)
time.sleep(2)  # Wait for 2 seconds to see the results

submit_elements = driver.find_elements(By.XPATH, "//li[@id='search-5']//input[@value='»']")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='YouTube Playlists']")))

youToube_list_link = driver.find_element(By.CSS_SELECTOR, "a[title='YouTube Playlists']")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "a[title='YouTube Playlists']")))
time.sleep(3)  # Wait for 5 seconds to see the browser

driver.quit()

"""

"""
Test case #1
Step 1. Go to “https://practice.cydeo.com/”
Step 2. Click on “Registration Form”
Step 3. Enter “wrong_dob” into date of birth input box .    
Step 4. Verify that warning message is displayed: “The date of birth is not valid”
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
