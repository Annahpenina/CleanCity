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
