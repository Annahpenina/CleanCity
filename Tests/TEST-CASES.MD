✅TEST CASES 
------------------------------------------------------------------------------------------------------------------------------------------------------------------

---
📋 CleanCity App – QA Test Cases  

Author: Vuthlari Mabaso 

Last Updated: 16 July 2025

Project: CleanCity  

Scope:

End-to-end functional, non-functional, accessibility, and boundary test cases

---

**Content**
1. Functional Test Cases
2. Non-Functional Test Cases
3. Accessibility Test Cases
4. Boundary & Negative Test Cases
5. Cross-Browser Compatibility
6. Bug Reference Table

---

### Functional Test Cases

| TC ID  | Title                         | Preconditions         | Steps                                                                 | Expected Result |                      
|--------|-------------------------------|-----------------------|-----------------------------------------------------------------------|--------------------- |
| TC-01  | User Registration             | Open App in browser   | 1. Go to registration<br>2. Enter valid name, email, password<br>3. Click Register | Success message appears, user added    |          |         |
| TC-02  | User Login                    | User account exists   | 1. Go to login<br>2. Enter valid email, password<br>3. Click Login    | Redirected to dashboard                |          |         |
| TC-03  | Invalid Login Attempt         | None                  | 1. Go to login<br>2. Enter invalid email/password<br>3. Click Login   | Error: "Invalid credentials"           |          |         |
| TC-04  | Submit Waste Pickup Request   | User logged in        | 1. Open pickup form<br>2. Enter address, date, waste type<br>3. Click Submit | Request submitted, form resets         |          |         |
| TC-05  | Submit Feedback Form          | App loaded            | 1. Fill name, rating, comment<br>2. Click Submit                      | "Thank you" message, form cleared      |          |         |
| TC-06  | Admin Dashboard Loads Requests| Admin logged in       | 1. Log in as admin<br>2. Go to dashboard                              | Table of pickup requests visible       |          |         |
| TC-07  | Update Pickup Status (Admin)  | Admin on dashboard    | 1. Click "Update" on request<br>2. Change status<br>3. Save           | Status updates immediately             |          |         |
| TC-08  | Filter Requests by Status     | Admin on dashboard    | 1. Select status filter<br>2. Click Apply                             | Only filtered status requests shown    |          |         |
| TC-09  | Filter Requests by Location   | Admin on dashboard    | 1. Select location filter<br>2. Click Apply                           | Only filtered location requests shown  |          |         |
| TC-10  | Filter by Status & Location   | Admin on dashboard    | 1. Select both filters<br>2. Click Apply                              | Only requests matching both shown      |          |         |

---

### Non-Functional Test Cases

| TC ID   | Title                      | Preconditions     | Steps                                  | Expected Result                  | 
|---------|----------------------------|-------------------|----------------------------------------|----------------------------------|
| TC-NF1  | Performance - Form Load    | App loaded        | Load request form 20x in 1 min         | No lag, loads <1s each time      |   
| TC-NF2  | Load - Dashboard           | App loaded        | Simulate 200 concurrent users on dashboard | Loads <2s, no visible slowdown  |   
| TC-NF3  | Security - SQLi            | App loaded        | Enter SQLi payloads in login/registration | Malicious input rejected, app not compromised |       

---

### Accessibility Test Cases

| TC ID      | Title                        | Preconditions     | Steps                                   | Expected Result            | 
|------------|------------------------------|-------------------|-----------------------------------------|----------------------------|
| TC-ACC1    | Screen Reader - Labels & Buttons | App loaded    | Use NVDA/VoiceOver, tab through all controls | All controls read correctly | 
| TC-ACC2    | Image Alt Text               | Awareness page    | Tab to each image, use screen reader    | Each image's purpose is announced |

---

### Boundary & Negative Test Cases

| TC ID       | Field      | Input/Scenario        | Expected Behaviour         | Actual                 | Bug Ref        |
|-------------|------------|----------------------|---------------------------|------------------------|----------------|
| TC-BOUND1   | Name       | 500 chars            | Truncated or error shown  | Accepts, breaks mobile | BUG-BOUND-01   |
| TC-BOUND2   | RequestID  | "REQ" + 100 chars    | Error or reject           | JS heap crash          | BUG-BOUND-02   |
| TC-BOUND3   | Date       | Empty                | "Please select valid date" error | No error shown    | BUG-FV-01      |
| TC-BOUND4   | Password   | <6 chars             | Error: "Min length 6"     | No error               | BUG-FV-02      |
| TC-BOUND5   | Register   | Mismatched passwords | Error: "Passwords do not match" | No error         | BUG-FV-03      |

---

### Cross-Browser Compatibility

| TC ID   | Title                | Preconditions | Steps                            | Expected Result                | 
|---------|----------------------|--------------|----------------------------------|-------------------------------|
| TC-XB1  | Chrome v138          | App deployed | Open app, use all main features  | No layout/functionality issues |         
| TC-XB2  | Firefox v140         | App deployed | Open app, use all main features  | No layout/functionality issues |               
| TC-XB3  | Safari (macOS/iOS)   | App deployed | Open app, use all main features  | No layout/functionality issues |      
| TC-XB4  | Edge v138            | App deployed | Open app, use all main features  | No layout/functionality issues |       

---

### Bug Reference Table

| Bug ID         | Description                 | Severity | Status | Linked Test Case(s)    |
|----------------|----------------------------|----------|--------|------------------------|
| BUG-FV-01      | Missing date validation     | Medium   | Open   | TC-BOUND3              |
| BUG-FV-02      | Password min length missing | Medium   | Open   | TC-BOUND4              |
| BUG-FV-03      | Passwords not matched       | Medium   | Open   | TC-BOUND5              |
| BUG-FILT-01    | Hardcoded filter            | High     | Open   | TC-08, TC-09           |
| BUG-ACC-01     | Missing alt-text on images  | Medium   | Open   | TC-ACC2                |
| BUG-UI-01      | UI does not auto-update     | Medium   | Open   | TC-07                  |
| BUG-BOUND-01   | Name >100 chars accepted    | Medium   | Open   | TC-BOUND1              |
| BUG-BOUND-02   | RequestID heap overflow     | High     | Open   | TC-BOUND2              |

---
