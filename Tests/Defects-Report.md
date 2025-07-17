## 🐞 Defects Report
------------------------------------------------------------------------------------------------------------------------------------------------------------------

📚 Title : Input

📰 Description : Full Name ID field accepts long inputs 

Environment : Chrome

Severity : Minor

Priority : High



📚 Title : Form Validation and Usability 

📰 Description : No feedback on successful/failed form submission: Success and error messages are present but hidden by default; unclear if they are shown on actual submission. 

Environment : Chrome 

Severity : Minor 

Priority : High 




📚 Title : Security Concerns regarding login details

📰 Description : Demo credentials: Demo accounts are shown on the login page, which is fine for a demo but should be removed for production.

Environment : Chrome 

Severity : Critical 

Priority : Low - Remove before production





📚 Title : User Experience

📰 Description : No loading indicators: No feedback for users during async operations (e.g., form submission, dashboard loading).

Environment : Chrome 

Severity : Critical 

Priority : High




# Defects Report for CleanCity

**Document:** CleanCity  
**Date:** 11/07/2025  
**Reviewer:** Vuthlari Mabaso

---

## 1. Accessibility Issues

| ID         | Description                                                                 | Severity | Location/Reference                | Recommendation                        |
|------------|-----------------------------------------------------------------------------|----------|------------------------------------|----------------------------------------|
| ACC-01     | Images in Awareness section missing `alt` attributes                        | Medium   | Awareness Page (all `<img>`)       | Add descriptive `alt` text to images   |
| ACC-02     | Error messages not associated with inputs via `aria-describedby`            | Low      | All forms                          | Add `aria-describedby` to inputs       |
| ACC-03     | No skip-to-content or landmark navigation for screen readers                | Low      | Whole document                     | Add skip links/landmarks               |
| ACC-04     | Some labels for radio buttons lack `for` attribute (uses wrapping instead)  | Low      | Waste Type radio group             | Use `for` attribute for each input     |

---

## 2. Form Validation & Usability

| ID         | Description                                                                 | Severity | Location/Reference                | Recommendation                        |
|------------|-----------------------------------------------------------------------------|----------|------------------------------------|----------------------------------------|
| FV-01      | Register form password field does not enforce minimum length in HTML        | Medium   | Register Page                      | Add `minlength="3"` to password input  |
| FV-02      | Register form does not validate password and confirm password match         | Medium   | Register Page                      | Add JS validation for password match   |
| FV-03      | Feedback form Request ID field allows excessive input length                | Medium   | Feedback Page                      | Add `maxlength` attribute              |
| FV-04      | Home form: Date field is optional, but no validation for invalid dates      | Low      | Home Page                          | Add date validation if needed          |

---

## 3. UI/UX Issues

| ID         | Description                                                                 | Severity | Location/Reference                | Recommendation                        |
|------------|-----------------------------------------------------------------------------|----------|------------------------------------|----------------------------------------|
| UI-01      | UI does not auto-update after status change in Admin Panel                  | Medium   | Admin Page                         | Add state sync after update            |
| UI-02      | No loading indicators for async actions (e.g., form submission)             | Low      | All forms                          | Add loading spinners/feedback          |


---

## 4. Security Concerns

| ID         | Description                                                                 | Severity                                      | Location/Reference                 |                     
|------------|-----------------------------------------------------------------------------|---------------------------------------------- |------------------------------------|
| SEC-01     | Password fields lack `autocomplete` attributes                              | Low                                           | Login/Register Pages               |      |
| SEC-02     | Demo credentials visible on login page                                      | Info(remove before production of application) | Login Page                         |

---

## 6. Boundary & Input Handling

| ID         | Description                                                                 | Severity | Location/Reference                 |                        
|------------|-----------------------------------------------------------------------------|----------|------------------------------------|
| BOUND-01   | Name and Request ID fields accept very long input, breaking layout          | Medium   | Home/Feedback Pages                | 

         |

---

## Summary Table 

| ID        | Severity | Short Description                        |
|-----------|----------|------------------------------------------|
| ACC-01    | Medium   | Awareness images missing alt text        |
| FV-01     | Medium   | Register password min length not enforced|
| FV-02     | Medium   | Register password match not validated    |
| FV-03     | Medium   | Feedback Request ID allows long input    |
| UI-01     | Medium   | Admin status change needs UI refresh     |
| BOUND-01  | Medium   | Name/Request ID fields allow long input  |
| ...       | ...      | ...                                      |

---

Software Tester: Vuthlari Mabaso






