import traceback

def test_admin_panel():
    # Setup Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    url = "http://localhost:5500"  

    try:
        driver.get(url)
        print("Page loaded")

        # Login steps...
        login_nav = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-page="login"]')))
        login_nav.click()
        print("Navigated to login")

        wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        driver.find_element(By.ID, "login-email").send_keys("admin@cleancity.com")
        driver.find_element(By.ID, "login-password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()
        print("Login submitted")

        wait.until(EC.visibility_of_element_located((By.ID, "user-links")))
        print("Logged in successfully")

        # Navigate to admin
        admin_link = wait.until(EC.element_to_be_clickable((By.ID, "admin-link")))
        admin_link.click()
        print("Admin page clicked")

        wait.until(EC.visibility_of_element_located((By.ID, "admin-page")))
        print("Admin page loaded")

        # Check dropdowns and button
        request_select = wait.until(EC.presence_of_element_located((By.ID, "requestSelect")))
        status_select = wait.until(EC.presence_of_element_located((By.ID, "statusSelect")))
        update_button = driver.find_element(By.ID, "updateStatusBtn")

        select_requests = Select(request_select)
        print(f"Number of requests in dropdown: {len(select_requests.options)}")
        if len(select_requests.options) < 2:
            print("No requests available to update.")
            return

        select_requests.select_by_index(1)

        select_status = Select(status_select)
        select_status.select_by_visible_text("Scheduled")

        wait.until(EC.element_to_be_clickable((By.ID, "updateStatusBtn")))
        update_button.click()
        print("Update button clicked")

        time.sleep(2)

        # Verify update in table
        admin_table_body = driver.find_element(By.ID, "admin-tbody")
        rows = admin_table_body.find_elements(By.TAG_NAME, "tr")

        updated = False
        selected_request_id = select_requests.first_selected_option.get_attribute("value")
        print(f"Selected request ID: {selected_request_id}")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 5:
                request_id = cells[0].text.strip()
                status = cells[5].text.strip()
                print(f"Row: {request_id}, Status: {status}")
                if request_id == selected_request_id and status == "Scheduled":
                    updated = True
                    break

        assert updated, "Request status was not updated correctly."
        print("Admin status update test passed successfully.")

        logout_btn = wait.until(EC.element_to_be_clickable((By.ID, "logout-btn")))
        logout_btn.click()
        print("Logged out")

        wait.until(EC.visibility_of_element_located((By.ID, "auth-links")))
        print("Back to login page")

    except Exception as e:
        print("Exception occurred:")
        traceback.print_exc()
    finally:
        driver.quit()
