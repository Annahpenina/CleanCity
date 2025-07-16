✅TEST CASES 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#. Test Environment Setup 
# Pre-Test Configuration 
Step| Action                | Verification                                 | Screenshot Reference |    Results                            |
| --| ----------------------| ---------------------------------------------| -------------------- | --------------------------------------|
| 1 | Clear browser cache   | DevTools → Network → "Disable cache" checked | [Cache Clear]        | Console tab active, no errors on load |
| 2 | Open DevTools(F12)    | Console tab active, no errors on load        | [DevTools Open]      | Console tab active, no errors on load |
| 3 | Navigate to Home Page | URL: http: // localhost: 3000                | [Home Page]          | Home page loaded successfully         |



Technical Validation: 
// Verify clean localStorage 
console.log(localStorage.length);  // Should return 0 
#. Detailed Test Execution 
✅# Form Validation Testing 
TC-FV-01: Required Field Validation 
Test Data: 
"scenario": "Empty submission", 
"fields": ["name", "location", "wasteType", "date"] 
Procedure: 
1. Navigate to Home Page  
2. Click "Submit Request" without entering data 
3. Inspect DOM for error elements: 
javascript 
document.querySelectorAll('.error-message').length // Expected: 3


✅Expected vs ❌Actual:
| Field               | Expected Error                       | Actual Result                        | Bug Reference |
|---------------------|--------------------------------------|--------------------------------------|---------------|
| Date                | "Please select valid date"           | No error shown                       | BUG - FV -    |
| Name                | "Please fill in this field"          | "Please fill in this field"          |               |
| Location            | "Please fill in this field"          | "Please fill in this field"          |               |
| WasteType           | "Please select one of these options" | "Please select one of these options" |               |
| Console Monitoring: | [Form Valida on] Missing valida on for: dateField |
   

# Filter Functionality Testing 
TC-FILT-01: Loca on Filter Accuracy 
Test Matrix:
 
| Filter  | Outcome          | Actual Outcome       | Bug 
| --------| ---------------- | -------------------- | ----------------
| Eldoret | Eldoret Requests | Nairobi Requests     |



Debugging Steps: 
1. Execute in Console: 
javascript 
// Check filter func on logic 
console.log(filterRequests.toString()); 
2. Iden fied Issue: 
javascript 
// Hardcoded filter (bug) 
return requests.filter(req => req.loca on === "Nairobi"); 
Visual Evidence: 
// a ach screenshot

3.3 Accessibility Tes ng 
TC-ACC-01: Image Alt-Text Verifica on 
Screen Reader Test Protocol: 
1. Launch NVDA screen reader 
2. Navigate to Awareness Page  
3. Tab through images while monitoring output: 
Expected Output: 
"Image: Waste sor ng diagram" 
Actual Output: 
"Image: Unlabeled" (repeated 3 mes) 
HTML Analysis: 
html 
<!-- Bug Demonstration --> 
<img src="waste.jpg"> <!-- Missing alt a ribute --> 
Lighthouse Audit Results: 
Accessibility Score: 89/100 
Missing alt - text: 3 items
 
# UI State Testing 
TC-UI-01: Real-Time Status Updates 
Test Procedure: 
1. Admin Panel → Select REQ005 
2. Change status: Pending → Scheduled 
3. Monitor: 
• UI update latency 
• localStorage changes 
Data Flow Verifica on: 
diff 
# localStorage Diff 
{ -     
"requests": [ 
{ 
"id": "REQ005", 
"status": "Pending", 
+     
"status": "Scheduled" 
} 
] 
} 
Observed Behavior: 
• UI requires manual refresh to reflect changes 
• Root Cause: Missing state synchroniza on

# Boundary Testing 
TC - BOUND - 0 1: Extreme Input Handling

Test Cases:
| field     | Input Type        | Expected Behavior | Actual Behavior | Device Impact            |
| --------- | ----------------- | ----------------- | --------------- | ------------------------ |
| Name      | 500 chars         | Truncate/Error    | Accepts         | Mobile layout break      |
| RequestID | "REQ" + 100 chars | Error             | Accepts         | Crashes JS heap overflow |



Console Warnings: 
[Input Valida on] 512 - char input exceeds recommended 100 - char limit


 # 🐞Defect Documentation 
# Confirmed Bugs 
| ID               | Description                        | Severity | Technical Root Cause                  |
| ---------------- | ---------------------------------- | -------- | ------------------------------------- | 
| BUG - FV - 0 1   | Missing date validation            | Medium   | No event listener for date input      |
| BUG - FILT - 0 1 | Hardcoded filter                   | High     | Static value in filterRequests()      |
| BUG-FV-02         | Password min length not enforced   | Medium   | No minlength attribute or JS check    |
| BUG-FV-03        | Passwords not matched on register  | Medium   | No JS validation for confirm password |
| BUG-FILT-01      | Hardcoded filter                   | High     | Static value in filterRequests()      |
| BUG-ACC-01       | Missing alt-text                   | Medium   | No alt attribute on images            |
| BUG-UI-01        | UI does not auto-update on status  | Medium   | No state sync after update            |
| BUG-BOUND-01     | Name field accepts 500+ chars      | Medium   | No maxlength or truncation            |
| BUG-BOUND-02     | RequestID field heap overflow      | High     | No input length validation            |



Sign-Off:  
Software Tester:  Vuthlari Mabaso
Date: 11/07/2025




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

| TC ID  | Title                         | Preconditions         | Steps                                                                 | Expected Result                        | Actual   | Bug Ref |
|--------|-------------------------------|-----------------------|-----------------------------------------------------------------------|----------------------------------------|----------|---------|
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

| TC ID   | Title                      | Preconditions     | Steps                                  | Expected Result                  | Actual   | Bug Ref |
|---------|----------------------------|-------------------|----------------------------------------|----------------------------------|----------|---------|
| TC-NF1  | Performance - Form Load    | App loaded        | Load request form 20x in 1 min         | No lag, loads <1s each time      |          |         |
| TC-NF2  | Load - Dashboard           | App loaded        | Simulate 200 concurrent users on dashboard | Loads <2s, no visible slowdown  |          |         |
| TC-NF3  | Security - SQLi            | App loaded        | Enter SQLi payloads in login/registration | Malicious input rejected, app not compromised | |         |

---

### Accessibility Test Cases

| TC ID      | Title                        | Preconditions     | Steps                                   | Expected Result            | Actual   | Bug Ref |
|------------|------------------------------|-------------------|-----------------------------------------|----------------------------|----------|---------|
| TC-ACC1    | Screen Reader - Labels & Buttons | App loaded    | Use NVDA/VoiceOver, tab through all controls | All controls read correctly |       |         |
| TC-ACC2    | Image Alt Text               | Awareness page    | Tab to each image, use screen reader    | Each image's purpose is announced |    |         |

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

| TC ID   | Title                | Preconditions | Steps                            | Expected Result                | Actual   | Bug Ref |
|---------|----------------------|--------------|----------------------------------|-------------------------------|----------|---------|
| TC-XB1  | Chrome v138          | App deployed | Open app, use all main features  | No layout/functionality issues |         |         |
| TC-XB2  | Firefox v140         | App deployed | Open app, use all main features  | No layout/functionality issues |         |         |
| TC-XB3  | Safari (macOS/iOS)   | App deployed | Open app, use all main features  | No layout/functionality issues |         |         |
| TC-XB4  | Edge v138            | App deployed | Open app, use all main features  | No layout/functionality issues |         |         |

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
