"""
Test case #9
Step 1. Go to “https://practice.cydeo.com/”
Step 2. And click on “Status Codes”.
Step 3. Then click on “200”, "301", "404", and "500" as SC.
Step 4. Verify that following message is displayed:
“This page returned a {SC} status code”



"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test data: status codes and their expected messages
test_data = [
    ("200", "This page returned a 200 status code"),
    ("301", "This page returned a 301 status code"),
    ("404", "This page returned a 404 status code"),
    ("500", "This page returned a 500 status code"),
]

@pytest.fixture(scope="function")
def driver():
    # Setup: Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown: Quit the WebDriver
    driver.quit()

@pytest.mark.parametrize("status_code, expected_message", test_data)
def test_status_codes(driver, status_code, expected_message):
    # Step 1: Go to the website
    driver.get("https://practice.cydeo.com/")

    # Step 2: Click on "Status Codes"
    status_codes_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Status Codes"))
    )
    status_codes_link.click()

    # Step 3: Click on the status code link
    status_code_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, status_code))
    )
    status_code_link.click()

    # Step 4: Verify the message
    message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "p"))
    )
    actual_message = message_element.text
    assert expected_message in actual_message, f"Expected '{expected_message}', but got '{actual_message}'"

