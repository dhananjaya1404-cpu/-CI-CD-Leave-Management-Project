# 📅 LeaveSync — Employee Leave Management System

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black?style=flat&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat&logo=githubactions)

A real-world **Employee Leave Management System** built with Python & Flask. Employees can apply for leaves, track status, and managers can approve or reject requests — all through a clean dashboard UI. Fully containerized with Docker and automated with a CI/CD pipeline using GitHub Actions.

---

## 🖥️ Application Preview

| Dashboard | Apply Leave |
|---|---|
| Stats, balance bars, recent requests | Form with leave type, dates, reason |

| My Leaves | Admin Panel |
|---|---|
| Filter by status, leave history table | Approve / Reject pending requests |

---

## ✨ Features

- 📊 **Dashboard** — Live stats: leave balance, taken days, pending requests, team on leave today
- 📝 **Apply Leave** — Submit Annual, Sick, Casual, Maternity, Comp Off requests
- 📋 **My Leaves** — Personal leave history with status filter
- 👥 **Team Calendar** — View all team members' leave status
- ⚙️ **Admin Panel** — Approve or reject pending leave requests
- 🏥 **Health Check** — `/health` endpoint for monitoring
- 🐳 **Docker Ready** — Fully containerized, runs anywhere
- 🔁 **CI/CD Pipeline** — Auto lint, test, and Docker build on every push

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11, Flask 3.0 |
| Frontend | Jinja2 Templates, HTML5, CSS3 |
| Testing | Pytest, pytest-cov |
| Linting | Flake8 |
| Container | Docker |
| CI/CD | GitHub Actions |
| Storage | In-Memory (Python dict) |

---

## 📁 Project Structure

```
leave-management/
├── app.py                  # Main Flask application & routes
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container config
├── .github/
│   └── workflows/
│       └── cicd.yml        # GitHub Actions pipeline
├── static/
│   └── style.css           # Application styles
├── templates/
│   ├── base.html           # Base layout with sidebar
│   ├── dashboard.html      # Home dashboard
│   ├── apply.html          # Apply leave form
│   ├── my_leaves.html      # Personal leave history
│   ├── team.html           # Team leave calendar
│   └── admin.html          # Admin approval panel
└── tests/
    └── test_app.py         # Pytest test cases
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.11+
- pip
- Docker Desktop (for Docker run)
- Git

---

### 🔹 Method 1 — Run with Python (Local)

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/leave-management.git
cd leave-management
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the application**
```bash
python app.py
```

**4. Open browser**
```
http://localhost:5000
```
> Browser opens automatically when you run the app.

---

### 🔹 Method 2 — Run with Docker

**1. Build the Docker image**
```bash
docker build -t leavesync .
```

**2. Run the container**
```bash
docker run -p 5000:5000 leavesync
```

**3. Open browser**
```
http://localhost:5000
```

**Useful Docker commands**
```bash
# Run in background
docker run -d -p 5000:5000 --name leavesync-app leavesync

# Check running containers
docker ps

# View logs
docker logs leavesync-app

# Stop container
docker stop leavesync-app

# Remove container
docker rm leavesync-app
```

---

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov=app --cov-report=term-missing
```

## 🔁 CI/CD Pipeline

Every push to `main` branch triggers the GitHub Actions pipeline automatically.

```
Push to GitHub
      ↓
Job 1 → Lint Check (flake8)
      ↓ pass
Job 2 → Run Tests (pytest + coverage)
      ↓ pass
Job 3 → Docker Build + Health Check
      ↓ pass
Pipeline GREEN ✅
```

### Pipeline Jobs

| Job | Tool | What it does |
|---|---|---|
| Lint | flake8 | Checks code style and formatting |
| Test | pytest | Runs all test cases with coverage |
| Build | Docker | Builds image and validates `/health` endpoint |

### View Pipeline

1. Go to your GitHub repository
2. Click **Actions** tab
3. See live pipeline status for every push

---

## 👥 Sample Employees (Pre-loaded Data)

| ID | Name | Department | Role |
|---|---|---|---|
| E001 | Azam Z | Backend | Cloud Engineer |
| E002 | Dolly | Design | UI Designer |
| E003 | Akash H | Backend | DevOps Engineer |
| E004 | Manoj | QA | DevOps Engineer |
| E005 | Dhanush D | DevOps | Software Engineer |

---

## 📊 Leave Types Supported

| Type | Default Balance |
|---|---|
| Annual Leave | 18 days |
| Sick Leave | 6 days |
| Casual Leave | 4 days |
| Maternity Leave | 90 days |
| Comp Off | 2 days |

---

## 🗺️ Future Improvements

- [ ] Add database support (PostgreSQL / SQLite)
- [ ] User login and authentication
- [ ] Email notifications on approval / rejection
- [ ] Export leave report as PDF
- [ ] Deploy to cloud (Render / AWS / Railway)
- [ ] Docker Compose with database container
- [ ] Role-based access (Employee vs Manager vs Admin)

---
## 📄 License

This project is for educational purpose only.
