"""
Test case #7
Step 1. Go to “https://practice.cydeo.com/”
Step 2. And click on “File Upload".
Step 3. Upload any file with .txt extension from your
computer.
Step 4. Click “Upload” button.
Step 5. Verify that subject is: “File Uploaded!”
Step 6. Verify that uploaded file name is displayed.
Note: use element.sendKeys(“/file/path”) with
specifying path to the file for uploading. Run this
method against “Choose File” button.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)

driver.get("https://practice.cydeo.com/")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "File Upload")))

# Step 2. And click on “File Upload".
file_upload_link = driver.find_element(By.LINK_TEXT, "File Upload")

file_upload_link.click()

# Step 3. Upload any file with .txt extension from your computer.
file_input = driver.find_element(By.ID, "file-upload")
file_input.send_keys("/Users/ugurargun/Documents/test_file.txt")  

time.sleep(2)  # Just to visually confirm the input during the test run

# Step 4. Click “Upload” button.
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

# Step 5. Verify that subject is: “File Uploaded!”
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
success_message = driver.find_element(By.TAG_NAME, "h3")
assert success_message.is_displayed(), "Success message is not displayed"
assert success_message.text == "File Uploaded!", "Success message text does not match"
