CleanCity QA Test Report – Phase 2 & 3

Project: CleanCity App 

software Tester: Nompumele A. Mthembu

Report Date: 11 July 2025

Phases Covered: Phase 2 (Test Design), Phase 3 (Execution)


**Phase 2: Test Design**

**Test Objectives**
   - Verify that all features of the Clean City Waste Pickup Scheduler function correctly.
   - Validate the application’s performance under different conditions.
   - Ensure compatibility across various browsers and devices.


 **Test Scope**
|In Scope           	               |Out of Scope                 |
|-----------------------------------|-----------------------------|
|Waste pickup request forms 	      |Backend API (serverless)     |
|Feedback forms	                  |Payment systems              |
|Dashboard filtering	               |Real-time push notifications |


**Test Cases**
**Functional Test Cases**

|Test Case ID	|Title	                          |Preconditions	             |Steps to Execute 	                                                                                                       |Status     |
|---------------|---------------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|TC-01	        | User Registration	              | App is open in the browser | 1. Go to registration page 2. Enter valid details (name, email, password) 3. Click Register, a success message is shows   | Pass      |
|TC-02          | User Login	                  | User account exists        | 1. Go to login page 2. Enter valid email and password 3. Click Login	User is redirected to the dashboard	               | Pass      |
|TC-03          | Invalid Login Attempt           | None	                   | 1. Go to login page 2. Enter invalid email or password 3. Click Login	Error message: “Invalid credentials”               |Pass       |
|TC-04	        | Submit Waste Pickup Request     | User is logged in 	       | 1. Open the pickup request form 2. Fill in address, date, and issue 3. Click Submit	Request submitted, form resets to allow a new entry	|Pass       |                               
|TC-05          | Submit Feedback Form            | App is loaded	           | 1. Fill in name, rating, and comment 2. Click Submit	“Thank you” message shown; form is cleared                         | Pass     | 
|TC-06	        | Admin Dashboard Loads Requests  | Admin is logged in         | 1. Log in as admin 2. Navigate to /admin dashboard	A table of pickup requests is shown	                                   | Pass     |
|TC-07	        | Update Pickup Status (Admin)    | Admin is on dashboard      | 1. Click “Update” on a request 2. Change status to “Completed” 3. Save the change	Status updates immediately             |Pass      |
|TC-08	        | Filter Requests by Status       | Admin is on dashboard	   | 1. Select status filter (e.g., “Pending”) 2. Click Apply	Only requests with selected status are displayed	           | Pass     |
|TC-09	        | Filter Requests by Location     | Admin is on dashboard	   | 1. Select location filter (e.g., “Nirobi”) 2. Click Apply	Only requests for selected location are displayed	       |Pass      |
|TC-10	        | Filter Requests by Status and Location | Admin is on dashboard| 1. Select status and location filters 2. Click Apply	Only requests matching both filters are displayed	               |Pass      |
|TC-11	        | Accessibility Check (Screen Reader) | App is loaded	        | 1. Use NVDA or VoiceOver 2. Navigate through the app	All labels and buttons are read correctly	                       |Pass      |
|TC-12	        | Cross-Browser Compatibility     | App is loaded in different browsers| 1. Open in Chrome, Firefox, Safari, Edge 2. Check layout and functionality	No layout issues or broken features|Pass      |   
|TC-13          | Response Time                   | Load Dashboard              | Loads < 2 seconds         |Pass      |
|TC-14          | Tab Navigation                  | Navigate with Tab Key       | All interactive elements reachable   | Pass      |

```

**Non-Functional Test Cases**

|Test Case ID| Title          | Preconditions            | Steps to Execute	         	                                 | Status            |
|------------|----------------|--------------------------|-----------------------------------------------------------------|-------------------|
|TC-NF1	    | Performance Testing	| App is loaded	   |Simulate multiple users submitting waste pickup requests simultaneously |	Pass       |
|TC-NF2	    | Load Testing	| App is loaded	         |Use a tool to simulate 200 concurrent users on the dashboard	Dashboard loads within 2 seconds without performance degradation	|	Pass       |
|TC-NF3     | Security Testing| None	                  | Attempt SQL injection on the login and registration forms	The application should reject malicious inputs without compromising data integrity 	|	Pass       |

```

**Cross-Browser Testing** (via BrowserStack)
**Browsers tested:**
- Google Chrome v138
- Mozilla Firefox v140
- Apple Safari (macOS + iOS)
- Microsoft Edge v138

Key outcomes:
- All forms, filters, and dashboards rendered correctly.
```

**Test cases summary**
|Category	   |Total   | Tests	|Passed	|Failed |
|--------------|--------|--------|--------|-------|
|Functional	   | 14	   | 14	   | 14     | 0     |
|Non-Functional| 3      | 3      |	3     | 0     |
|Accessibility | 2	   | 2	   | 2      | 0     |
|Cross-Browser | 1      | 1      | 1      | 0     |
```

**Test Users and Sample Content**
User Role	Test User Account	Purpose
Regular	testuser@example.com	Pickup & feedback test
Admin	admin@cleancity.gov	Dashboard, filters, status updates

Sample Data Created:
- 5 pickup requests (various cities/status)
- 3 feedback entries (mixed ratings/comments)

Admin dashboard preloaded with dummy data
Data available in localStorage (simulated backend)



**Phase 3: Test Execution**

**Test Execution Summary**
Test Executed: All planned test cases were executed as defined in Phase 2.
Test Results: A total of 14 functional test cases and 3 non-functional test cases were executed.
Results Overview:

Total Test Cases: 17
Passed: 17
Failed: 0
Blocked: 0


**Test Execution Log**

|Test Case ID | Title	                               | Execution Date | Executor              | Status       	| Comments                |
|-------------|----------------------------------------|----------------|-----------------------|-----------------|-------------------------------|
|TC-01	     | User Registration	                   | 09/07/20205	    | Nompumelelo Mthembu	| Pass	         | Successfully registered |
|TC-02        | User Login	                            | 09/07/20205     | Nompumelelo Mthembu  | Pass	         | Successfully logged in  |
|TC-03        | Invalid Login Attempt                  | 09/07/20205	    | Nompumelelo Mthembu  | Pass	         | Correct error message displayed |
|TC-04        | Submit Waste Pickup Request            | 09/07/20205     | Nompumelelo Mthembu 	| Pass	         | Form reset after submission |
|TC-05        | Submit Feedback Form                   | 09/07/20205     | Nompumelelo Mthembu  | Pass	         | Thank you message shown     |
|TC-06	     | Admin Dashboard Loads Requests         | 09/07/20205      | Nompumelelo Mthembu  | Pass	         | Dashboard loaded with requests |
|TC-07        | Update Pickup Status (Admin)           | 09/07/20205	    | Nompumelelo Mthembu   | Pass	         | Status updated correctly    |
|TC-08        | Filter Requests by Status	             | 09/07/20205     | Nompumelelo Mthembu   | Pass	         | Proper filtering implemented   |
|TC-09        | Filter Requests by Location            | 09/07/20205     |Nompumelelo Mthembu    | Pass	         | Proper filtering implemented   |
|TC-10        | Filter Requests by Status and Location |	09/07/20205     | Vuthlari Mabaso   | Pass	         | Correct requests displayed      |
|TC-11        | Accessibility Check (Screen Reader)    |	09/07/20205	    |  Vuthlari Mabaso   | Pass	         | All elements correctly read    |
|TC-12        | Cross-Browser Compatibility            | 09/07/20205	    |  Vuthlari Mabaso   | Pass           | No issues found across browsers|
|TC-13	     | Response Time	                         | 09/07/20205	    |  Vuthlari Mabaso   | Pass	         | Loaded within expected time    |
|TC-14	     | Tab Navigation	                      | 09/07/20205     |  Vuthlari Mabaso   | Pass   	      | All elements accessible via Tab|
|TC-NF1	     | Performance Testing	                   | 09/07/20205	    |  Vuthlari Mabaso   | Pass	         | Application performed well under load   |
|TC-NF2	     | Load Testing	                        | 09/07/20205	    |  Vuthlari Mabaso   | Pass	         | Met load testing criteria      |
|TC-NF3       | Security Testing                      | 09/07/20205      |  Vuthlari Mabaso   | Pass	         | No vulnerabilities found       |

```
**Bug Summary**
**Defects Logged**
|ID      	| Title	                           | Severity  | Status   |
|-----------|-----------------------------------|-----------|----------|
|BUG-001	   | Login link at the footer	         | Medium	   | Open     |
|BUG-002    | Register link at the footer	      | Low	      | Open     |
|BUG-003    | Feedback page                     | Low	      | Open     |
|BUG-004    | Dash board page - admin login     | Low       | Open     |
|BUG-103    | Feedback page - admin login       | Low	      | Open     |
```

**Tools Used**
- Jira: Test management & bug tracking
- Browserstack: BrowserStack – Cross-browser testing
- Netlify - Deployment link: https://cleancityqa.netlify.app/
```


Sign-Off:  
Software Tester: Nompumelelo A. Mthembu
Date: 11/07/2025
