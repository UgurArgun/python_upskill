
"""
Step 1. Go to “https://practice.cydeo.com/”
Step 2. Click on “Registration Form”
Step 3. Enter any valid first name.
Step 4. Enter any valid last name.
Step 5. Enter any valid user name.
Step 6. Enter any valid password.
Step 7. Enter any valid phone number.
Step 8. Select gender.
Step 9. Enter any valid date of birth.
Step 10. Select any department.
Step 11. Enter any job title.
Step 12. Select java as a programming language.
Step 13. Click Sign up.
Step 14. Verify that following success message is
displayed: “You've successfully completed
registration!”
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)
driver.get("https://practice.cydeo.com/")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Registration Form")))
# Step 2: Click on "Registration Form"
registration_form_link = driver.find_element(By.LINK_TEXT, "Registration Form")
registration_form_link.click()

# Step 3: Enter any valid first name.
first_name_input = driver.find_element(By.NAME, "firstname")
first_name_input.send_keys("John")
# Step 4: Enter any valid last name.
last_name_input = driver.find_element(By.NAME, "lastname")
last_name_input.send_keys("Doe")
# Step 5: Enter any valid user name.
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys("johndoe")
# Enter a valid email address.
email_input= driver.find_element(By.NAME, "email")
email_input.send_keys("sarper@gmail.com")

# Step 6: Enter any valid password.
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Password123")
# Step 7: Enter any valid phone number.
phone_input = driver.find_element(By.NAME, "phone")

phone_input.send_keys("123-456-7890")

# Step 8: Select gender
gender_radio_button = driver.find_element(By.CSS_SELECTOR, "input[value='male']")
gender_radio_button.click()
assert gender_radio_button.is_selected

# Step 9: Enter any valid date of birth.
dob_input = driver.find_element(By.NAME, "birthday")
dob_input.send_keys("01/01/1990")   
# Step 10: Select any department.
# Select "Department of Engineering" first to open the dropdown
department_dropdown = driver.find_element(By.NAME, "department")
department_dropdown.send_keys("Department of Engineering")
assert department_dropdown.is_selected

# Then select "MCR"
select_option = Select(department_dropdown)
select_option.select_by_visible_text("MCR")
assert select_option.first_selected_option.text == "MCR" 

# Then select "Department of Agriculture"
options= department_dropdown.find_elements(By.TAG_NAME, "option")
for option in options:
    if option.text == "Department of Agriculture":
        option.click()
        break
assert option.is_selected(), "Department of Agriculture is not selected"

# Step 11: Enter any job title
job_title_dropdown = driver.find_element(By.NAME, "job_title")
job_title_dropdown.send_keys("SDET")
assert job_title_dropdown.is_selected

# Step 12: Select java as a programming language.
java_checkbox = driver.find_element(By.CSS_SELECTOR, "input[value='java']")
java_checkbox.click()
assert java_checkbox.is_selected()

# Step 13: Click Sign up.
sign_up_button = driver.find_element(By.ID, "wooden_spoon")
sign_up_button.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "p")))

# Step 14: Verify that following success message is displayed: “You've successfully completed registration!”
success_message = driver.find_element(By.TAG_NAME, "p")
assert success_message.is_displayed(), "Success message is not displayed"
assert success_message.text == "You've successfully completed registration!", "Success message text does not match"
driver.quit()

