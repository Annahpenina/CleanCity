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

    # go to dashboard
    driver.find_element(By.CSS_SELECTOR, 'a[data-page="dashboard"]').click()
    time.sleep(1)

    # apply a status filter
    Select(driver.find_element(By.ID, "statusFilter")).select_by_visible_text("Pending")
    time.sleep(1)
    capture_screenshot(driver, "dashboard_filtered_pending")

finally:
    driver.quit()
