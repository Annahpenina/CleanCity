import unittest, time
from selenium.webdriver.common.by import By
from utils import get_driver, take_screenshot

class TestLoginDashboard(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://cleancityqa.netlify.app/")

    def test_login_dashboard(self):
        driver = self.driver
        # Navigate to login page by clicking nav link
        driver.find_element(By.CSS_SELECTOR, '[data-page="login"]').click()
        time.sleep(1)

        # Fill in login form
        driver.find_element(By.ID, "login-email").send_keys("user@cleancity.com")
        driver.find_element(By.ID, "login-password").send_keys("password123")
        driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()

        # Wait and verify dashboard
        time.sleep(2)
        dashboard = driver.find_element(By.ID, "dashboard-page")
        self.assertTrue(dashboard.is_displayed())

        # Nav menu should now show user links
        user_links = driver.find_element(By.ID, "user-links")
        self.assertTrue(user_links.is_displayed())

        take_screenshot(driver, "login_dashboard_pass")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
