🧪 Selenium Test Report – Clean City App Project: Clean City – Waste Pickup Scheduler Tested by: QA Team Test Date: 16 July 2025 Test Environment:

OS: Windows 10 (64‑bit) Browser: Chrome 126.x Python: 3.11 / 3.13 Selenium: 4.x

App URL: https://cleancityqa.netlify.app/

Evidence Folder: C:\CleanCity\selenium\evidence\

⚙️ Setting Up the Environment Follow these steps to set up Selenium testing for the Clean City app on your machine:

✅ 1. Install Python

Download and install Python (3.11+ recommended) from https://www.python.org/downloads/. ✅ 2. Install Google Chrome
Install the latest version of Google Chrome. ✅ 3. Install ChromeDriver
Download ChromeDriver that matches your Chrome version from: https://chromedriver.chromium.org/downloads
Extract chromedriver.exe and place it in a folder that’s added to your PATH (or same directory as your tests).
powershell Copy Edit pip install selenium

powershell Copy Edit python -m venv venv .\venv\Scripts\activate pip install selenium ✅ 6. Run the Tests In PowerShell:

powershell Copy Edit

python test_login_dashboard.py python test_invalid_login.py python test_register_user.py python test_pickup_request.py python test_feedback_submission.py

NB: Screenshots will be stored automatically in the evidence folder.

Test Summary

Test Name	Script File	Objective	Status Evidence
Login → Dashboard (Valid Credentials)	test_login_dashboard.py	Verify login with valid user leads to dashboard	Pass
Invalid Login	test_invalid_login.py	Verify login with wrong credentials shows error	Pass
User Registration	test_register_user.py	Verify mismatched passwords show error message	Pass
Pickup Request Form	test_pickup_request.py	Verify required fields validation on pickup request	Pass
Feedback Submission	test_feedback_submission.py	Verify submitting feedback shows success message	Pass
Tools & Setup Tools Used:

Selenium WebDriver (Chrome)

Python unittest-style scripts

utils.py helper (driver setup and screenshot capture)

ChromeDriver installed and in PATH

Execution Commands:

powershell Copy code cd C:\CleanCity\selenium python test_login_dashboard.py python test_invalid_login.py python test_register_user.py python test_pickup_request.py python test_feedback_submission.py 📄 Detailed Test Cases & Results

Login → Dashboard Steps:
Open Clean City app
Navigate to Login
Enter user@cleancity.com / password123
Submit and verify dashboard page loads
Expected Result: Dashboard visible, nav menu changes to user links

Actual Result: As expected

Invalid Login Steps:
Open Login page
Enter invalid credentials
Submit
Expected Result: Error message displayed

Actual Result: Error alert shown (login-error div)

User Registration Steps:
Navigate to Register page
Fill valid name, email
Enter pass123 in password and differentpass in confirm password
Submit
Expected Result: Error message displayed for mismatched password

Actual Result: Register error alert displayed

Pickup Request Form Validation Steps:
Navigate to Home → Pickup form
Leave required fields blank
Click Submit
Expected Result: Form not submitted, browser highlights required fields
Actual Result: Validation prevented submission

Feedback Submission Steps:
Navigate to Feedback page
Enter REQ001 in Request ID
Select Missed Pickup
Enter comments and Submit
Expected Result: Success message displayed

Actual Result: Success alert displayed

📈 Test Metrics

Metric	Value
Total Tests Run	5
Passed	5
Failed	0
Evidence Captured	Yes
Overall Result: All automated Selenium tests passed successfully.

Prepared By: Nompumelelo Mthembu QA Team 📅 16 July 2025