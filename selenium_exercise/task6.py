"""
Test case #6
Step 1. Go to "https://www.fakemail.net/"
Step 2. Copy and save email as a string.
Step 3. Then go to “https://practice.cydeo.com/”
Step 4. And click on “Sign Up For Mailing List".
Step 5. Enter any valid name.
Step 6. Enter email from the Step 2.
Step 7. Click Sign Up
Step 8. Verify that following message is displayed:
“Thank you for signing up. Click the button below to
return to the home page.”
Step 9. Navigate back to the “https://
www.tempmailaddress.com/”
Step 10. Verify that you’ve received an email from
“do-not-reply@practice.cybertekschool.com”
Step 11. Click on that email to open it.
Step 12. Verify that email is from: “do-not-
reply@practice.cybertekschool.com”
Step 13. Verify that subject is: “Thanks for
subscribing to practice.cybertekschool.com!”
"""

#Step 1. Go to "https://www.fakemail.net/"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)
driver.get("https://www.fakemail.net/")
time.sleep(2)
#WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "color cetc")))

driver.find_element(By.XPATH, "(//*[text()='Manage options'])[1]").click()

# Wait for the element to be visible
confirm_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//*[text()='Confirm choices'])[1]"))
)

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)

# Click the element
confirm_button.click()
driver.implicitly_wait(5)
email = driver.find_element(By.ID, "email").text
print(email)
time.sleep(2)

# Step 3. Then go to “https://practice.cydeo.com/”
driver.get("https://practice.cydeo.com/")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up For Mailing List")))

# Step 4. And click on “Sign Up For Mailing List".
sign_up_link = driver.find_element(By.LINK_TEXT, "Sign Up For Mailing List")
sign_up_link.click()

# Step 5. Enter any valid name.
name_input = driver.find_element(By.NAME, "full_name")
name_input.send_keys("John Doe")

# Step 6. Enter email from the Step 2.
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(email)  # Use the email obtained from Step 2
time.sleep(2)

# Step 7. Click Sign Up
sign_up_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_up_button.click()
time.sleep(2)

# Step 8. Verify that following message is displayed:
success_message = driver.find_element(By.TAG_NAME, "h3")
assert success_message.is_displayed(), "Success message is not displayed"
assert success_message.text == "Thank you for signing up. Click the button below to return to the home page.", "Success message text does not match"
time.sleep(2)

# Step 9. Navigate back to the “https://www.fakemail.net/”
driver.get("https://www.fakemail.net/")
time.sleep(5)  # Wait for the email to arrive
driver.refresh()  # Refresh the page to load new emails

