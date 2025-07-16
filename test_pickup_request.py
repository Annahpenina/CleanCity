from utils import get_driver, capture_screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, os

HTML_FILE = os.path.abspath("..\\index.html")

driver = get_driver()
driver.get("file://" + HTML_FILE)

try:
    # login first
    driver.find_element(By.CSS_SELECTOR, 'a[data-page="login"]').click()
    time.sleep(1)
    driver.find_element(By.ID, "login-email").send_keys("user@cleancity.com")
    driver.find_element(By.ID, "login-password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()
    time.sleep(1)

    # go to home page
    driver.find_element(By.CSS_SELECTOR, 'a[data-page="home"]').click()
    time.sleep(1)

    # fill pickup form
    driver.find_element(By.ID, "fullName").send_keys("Automation Tester")
    Select(driver.find_element(By.ID, "location")).select_by_visible_text("Nairobi")
    driver.find_element(By.CSS_SELECTOR, "input[value='General']").click()
    driver.find_element(By.ID, "preferredDate").send_keys("2025-07-30")
    driver.find_element(By.CSS_SELECTOR, "#pickup-form button[type='submit']").click()
    time.sleep(2)

    capture_screenshot(driver, "pickup_submitted")

finally:
    driver.quit()
