# ✅ Cypress Test Report – E2E Auth → Dashboard  
**Project:** CleanCity – Waste Pickup Scheduler  
**Test Scenario:** End‑to‑End Authentication Flow (Login → Dashboard)
**QA Tester:** Nompumelelo A. Mthembu

---

## 🧪 Tools Used
| Tool | Purpose |
|------|---------|
| Cypress 14.5.1 | End‑to‑end testing framework |
| Node.js v22.14.0 | Runtime environment |
| npm | Dependency management |
| Electron 130 (Headless) | Browser used by Cypress in headless mode |
| CleanCity Web App | Hosted at [https://cleancityqa.netlify.app/](https://cleancityqa.netlify.app/) |

---

## 🌐 Test Environment
| Component | Version / Info |
|-----------|----------------|
| OS | Windows 11 x64 |
| Node.js | v22.14.0 |
| npm | 10.x |
| Cypress | 14.5.1 |
| Browser | Electron (Headless) |
| Test Spec | `cypress/e2e/auth_dashboard.cy.js` |

---

## 📋 E2E Test Case
**Test Name:** `should log in and navigate to dashboard successfully`

### Steps
1. Visit Login Page  
2. Navigate to `https://cleancityqa.netlify.app/`  
3. Enter valid credentials:  
   - **Email:** `user@cleancity.com`  
   - **Password:** `password123`  
4. Submit login form  
5. Assert that dashboard is displayed (`#dashboard-page` visible)

**✅ Expected Result:**  
- User is successfully redirected to Dashboard.  
- Dashboard content is visible (e.g., Pickup Requests table).

---

## 📊 Test Results
| Status | Duration | Screenshot |
|--------|----------|------------|
| ✅ Passed | 8.5s | See below |

**Run Command:**
```bash
npx cypress run --e2e --spec "cypress/e2e/auth_dashboard.cy.js"
