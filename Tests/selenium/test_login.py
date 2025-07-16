from utils import get_driver, capture_screenshot
from selenium.webdriver.common.by import By
import time, os

# path to your index.html
HTML_FILE = os.path.abspath("..\\index.html")

driver = get_driver()
driver.get("file://" + HTML_FILE)

try:
    # navigate to Login page
    driver.find_element(By.CSS_SELECTOR, 'a[data-page="login"]').click()
    time.sleep(1)

    # fill in login form
    driver.find_element(By.ID, "login-email").send_keys("user@cleancity.com")
    driver.find_element(By.ID, "login-password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()
    time.sleep(2)

    # check dashboard visible
    dashboard = driver.find_element(By.ID, "dashboard-page")
    assert dashboard.is_displayed(), "Dashboard should show after login"

    capture_screenshot(driver, "login_success")

finally:
    driver.quit()
