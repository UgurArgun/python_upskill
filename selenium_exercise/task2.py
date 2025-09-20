"""
Test case #2
Step 1. Go to “https://practice.cydeo.com/”
Step 2. Click on “Registration Form”
Step 3. Verify that following options for programming languages are displayed: c++, java,
JavaScript
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)

# Step 1. Go to “https://practice.cydeo.com/”
driver.get("https://practice.cydeo.com/")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h1'))) 

# Step 2: Click on "Registration Form"
driver.find_element(By.LINK_TEXT, "Registration Form").click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//h2')))

# Step 3: Verify that following options for programming languages are displayed: c++, java, JavaScript
Languages = ["C++", "Java", "JavaScript"]
for language in Languages:
    language_element = driver.find_element(By.XPATH, f"//label[.='{language}']")
    assert language_element.is_displayed(), f"{language} option is not displayed"

