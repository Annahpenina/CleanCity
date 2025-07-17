import unittest, time
from selenium.webdriver.common.by import By
from utils import get_driver, take_screenshot

class TestInvalidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://cleancityqa.netlify.app/")

    def test_invalid_login(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '[data-page="login"]').click()
        time.sleep(1)

        # Use wrong credentials
        driver.find_element(By.ID, "login-email").send_keys("wrong@cleancity.com")
        driver.find_element(By.ID, "login-password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()

        time.sleep(1)
        # Check error div
        error_div = driver.find_element(By.ID, "login-error")
        self.assertTrue(error_div.is_displayed())

        take_screenshot(driver, "invalid_login_pass")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
