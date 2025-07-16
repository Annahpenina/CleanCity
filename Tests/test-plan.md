# 🧪 Test Plan & Project Management for Clean City

**Version:** 1.0  
**Last Updated:** 2025-07-03
**Owner:** Quality Army  

---

## 📋 Project Management Requirements

**Platform:** Jira Cloud (free tier) or GitHub Kanban  
**Project Type:** Software Testing  
**Issue Types:** Bug, Task, Story, Epic  
**Workflow:** `To Do → In Progress → In Review → Done`  

### 🎯 Project Management Setup Instructions

- **Choose a Tool:**  
  - Use Jira (see Jira Setup Guide) or GitHub Kanban (see GitHub Projects docgit init
s)

- **Create Project Board:**  
  - Set up columns for workflow  
  - Add team members  
  - Configure issue types/cards  

### 📝 Project Management Usage Requirements

- **Daily Updates:** Log all testing activity  
- **Bug Reporting:** Create detailed bug reports (see template below)  
- **Progress Tracking:** Update task statuses daily  
- **Documentation:** Attach screenshots, test logs, and results  
- **Collaboration:** Assign and comment on tasks  

### 🔍 Bug Report Fields

- **Summary**: Clear bug title  
- **Description**: Steps to reproduce  
- **Environment**: OS, browser, device  
- **Severity**: Critical / Major / Minor / Cosmetic  
- **Priority**: High / Medium / Low  
- **Steps to Reproduce**: Numbered  
- **Expected vs Actual**  
- **Attachments**: Screenshots, logs, videos  

---

## 🏗️ Application Architecture

**Technology Stack:**  
- Frontend: React.js  
- Storage: localStorage (no backend)  
- Deployment: Netlify-ready  
- UI: Responsive, card-based, CleanCity branding  

### 🔑 Key Features to Test

#### 🔐 Authentication System
- Registration, login  
- Password validation & session management  
- Role-based access  

#### 🗑️ Core Waste Features
- Schedule waste pickup  
- Manage requests  
- Validate forms, persist to localStorage  

#### 📊 Dashboard & Analytics
- User stats, charts, gamification, real-time data  

#### 📝 Content System
- Blog articles, comments, feed posts  
- Likes, quizzes, admin moderation  

#### 👥 User Management
- User profiles & settings  
- Admin panel  
- Notifications & feedback

---

## 1. Testing Objectives

- Verify all core features meet requirements  
- Comply with **Municipal Data Privacy Act**  
- Simulate **10,000 concurrent users**  
- Ensure WCAG 2.1 AA accessibility compliance  
- Track all issues and activities using Jira or GitHub  

---

## 2. Testing Approach

### 🔹 Automation Strategy

| **Test Type**             | **Scope**                | **Tools**          | **Owner**           | 
|---------------------------|--------------------------|--------------------|---------------------|
| Unit                      | Core logic               | Jest / pytest      | Palesa Molefe       | 
| API (localStorage mocks)  | n/a                      | Supertest (mocked) | Vuthlari Mabaso     | 
| E2E                       | Auth → Dashboard         | Cypress            | Nompumelelo Mthembu | 
| Performance               | Load testing (simulated) | k6                 | QA Team             | 

**CI/CD:**  
- Tests run in GitHub Actions on push  
- Failing tests block merges  

---

### 🔹 Manual Testing

- **Exploratory:** Edge cases (blog posts, pickup timing)  
- **Accessibility:** axe-core, NVDA, keyboard nav  
- **Timebox:** 4 hours per sprint  
- **Device Testing:** Desktop, Tablet, Mobile  

---

## 3. Test Environment & Setup

- **Tools:** Node.js 18+, Python 3.10+, Docker  
- **Browsers:** Chrome, Firefox, Safari, Edge  
- **Test Devices:** Windows, macOS, iOS, Android  
- **Network Conditions:** 3G, 4G, WiFi  
- **Accessibility Tools:** axe, NVDA, VoiceOver  

---

## 4. Entry / Exit Criteria

### ✅ Entry

- SonarQube: <5% smells  
- ESLint: Zero critical errors  
- `npm run seed-test-data` complete  
- Project created in Jira with backlog ready

### ✅ Exit

- Unit pass rate ≥98%  
- No P0/P1 open bugs (Jira filter: `Release-2025Q3`)  
- All a11y issues resolved or accepted  
- Test cases linked to stories in [Traceability Matrix](docs/traceability.md)  

---

## 5. Deliverables

- `/tests/` - test suites  
- Allure or HTML reports  
- Bug log (Jira)  
- a11y checklist  
- Traceability matrix  
- Project board (Jira or GitHub)

---

## 6. Risk-Based Testing

- Focus on:  
  - Auth, Waste scheduling  
  - Admin control  
  - Forms & dashboards  
- Medium/low risk handled via exploratory

---

## 7. Browser & Device Matrix

| Platform  | Browsers              | Assistive Tech |
|-----------|-----------------------|----------------|
| Windows   | Chrome, Edge, Firefox | NVDA           |
| macOS     | Safari, Chrome        | VoiceOver      |
| Android   | Chrome                | TalkBack       |
| iOS       | Safari                | VoiceOver      |

---

## 8. STLC Implementation

### 🔹 Phase 1: Test Planning (Days 1–2)

- Define scope & objectives  
- Choose tools and workflows  
- Set up Jira + environments  
- Create seed data  

### 🔹 Phase 2: Test Design (Days 3–4)

- Write test cases (functional, non-functional, accessibility)  
- Cross-browser checklist  
- Create test users and sample content  

### 🔹 Phase 3: Test Execution (Days 5–8)

- Run functional and non-functional tests  
- Accessibility and compatibility testing  
- Log bugs in Jira / update statuses  

### 🔹 Phase 4: Test Closure (Days 9–10)

- Analyze bugs, finalize reports  
- Document defect metrics and risks  
- Deliver test summary and improvement plan  

---

## 9. Schedule

| **Phase**             | **Deadline**     |
|-----------------------|------------------|
| Unit Tests            | 2025-07-06       |
| API/E2E Tests         | 2025-07-10       |
| Accessibility Review  | 2025-07-14       |
| Load Testing          | 2025-07-15       |
| Closure & Reporting   | 2025-07-16       |

---

## 10. Setup Scripts

```bash
# Clone & install
git clone [repo-url] && cd clean-city
npm install

# Start DB
docker-compose -f test-env/docker-compose.yml up -d

# Run tests
npm test                  # Unit & Integration
npm run test:e2e --headed # E2E Debug

# Accessibility
npx axe-cli http://localhost:3000
