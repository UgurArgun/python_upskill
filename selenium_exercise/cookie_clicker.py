from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException  # Import the exception

from selenium.webdriver.support.ui import Select
import time

service = ChromeService(executable_path='')
driver = webdriver.Chrome(service=service)

# navigate to click cookies website
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(8)
# interact with robot popup and check that I'm a real person

# select the "Manage Options" button and click it
# select the "Confirm choises" button and click it
driver.maximize_window()
#driver.switch_to.frame("googlefcLoaded")
#driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//button[.="Manage options"]').click()
driver.find_element(By.XPATH, '//button[.="Confirm choices"]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//a[@class="cc_btn cc_btn_accept_all"]').click()
driver.implicitly_wait(5)

# Wait for the language selection element to be clickable and click it
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@id="promptContentChangeLanguage"]/div[@id="langSelect-EN"]'))
).click()

# Wait for the "big cookie" element to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# Attempt to click the "big cookie" with retry logic
while True:
    try:
        # Re-locate the "big cookie" element
        cookie = driver.find_element(By.ID, "bigCookie")
        # Click the "big cookie"
        cookie.click()
        break  # Exit loop if click is successful
    except StaleElementReferenceException:
        # Handle stale element by retrying
        continue

# Wait for the "cookie count" element to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "cookies"))
)
while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    for i in range(1, 8):
        try:
            item = driver.find_element(By.ID, f"product{i}")
            item_price = item.find_element(By.CLASS_NAME, "price").text
            item_price = int(item_price.replace(",", ""))
            if cookies_count >= item_price:
                item.click()
        except Exception as e:
            print(f"Could not purchase item {i}: {e}")
    print(cookies_count)

     
