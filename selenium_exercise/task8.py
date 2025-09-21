"""
Test case #8
Step 1. Go to “https://practice.cydeo.com/”
Step 2. And click on “Autocomplete”.
Step 3. Enter “United States of America” into
country input box.
Step 4. Click submit button.
Step 5. Verify that following message is displayed:
“You selected: United States of America”
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys as KEYS
import time

service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)

driver.get("https://practice.cydeo.com/")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Autocomplete")))

# Step 2. And click on “Autocomplete”.
autocomplete_link = driver.find_element(By.LINK_TEXT, "Autocomplete")
autocomplete_link.click()
time.sleep(2)

# Step 3. Enter “Turkey” into country input box.
country_input = driver.find_element(By.ID, "myCountry")
country_input.send_keys("Turkey")
time.sleep(2)  # Just to visually confirm the input during the test run
country_input.send_keys("\n")
time.sleep(2)

#Step 4. Click submit button.
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Submit']"))
)

# Scroll the button into view
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

# Try clicking the button
try:
    submit_button.click()
except:
    # If .click() doesn't work, use JavaScript to click
    driver.execute_script("arguments[0].click();", submit_button)

# Step 4. Verify that following message is displayed: “You selected: Turkey”
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "result")))

result_message = driver.find_element(By.ID, "result")
assert result_message.is_displayed(), "Result message is not displayed"
assert result_message.text == "You selected: Turkey", "Result message text does not match"
driver.quit()

