from utils import get_driver, capture_screenshot
from selenium.webdriver.common.by import By
import time, os

HTML_FILE = os.path.abspath("..\\index.html")

driver = get_driver()
driver.get("file://" + HTML_FILE)

try:
    # navigate to Register page
    driver.find_element(By.CSS_SELECTOR, 'a[data-page="register"]').click()
    time.sleep(1)

    # fill registration form
    driver.find_element(By.ID, "register-name").send_keys("Test User")
    driver.find_element(By.ID, "register-email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "register-password").send_keys("pass123")
    driver.find_element(By.ID, "register-confirm-password").send_keys("pass123")
    driver.find_element(By.CSS_SELECTOR, "#register-form button[type='submit']").click()
    time.sleep(2)

    capture_screenshot(driver, "register_success")
    print("✅ Registration form submitted")

finally:
    driver.quit()
