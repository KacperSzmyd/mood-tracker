![Tests](https://img.shields.io/github/actions/workflow/status/KacperSzmyd/mood-tracker/tests.yml?branch=main&label=tests&logo=github&style=flat-square)
![CI](https://github.com/KacperSzmyd/mood-tracker/actions/workflows/tests.yml/badge.svg)

# 🧠 Everyday Mood Tracker

A simple web application to track your daily mood, visualize it on a chart, and analyze your emotional trends over time.  
Perfect for self-reflection and mental health awareness 🧘‍♀️

---

## 🛠️ Tech stack

- Python 3.10
- Flask
- SQLite + SQLAlchemy
- Jinja2 templates
- Matplotlib
- Pytest
- GitHub Actions (CI)

---

## 🚀 Features

- 🔐 User registration & login (Flask-Login)
- 📅 Add mood (1–10 scale) with timestamp
- 📈 Mood chart with color-coded points:
  - 1–3 → 🔴 red (bad mood)
  - 4–6 → 🟠 orange (neutral)
  - 7–10 → 🟢 green (good mood)
- 📊 Weekly average mood
- 📥 Export data to CSV
- 🧪 Pytest-based test suite + GitHub Actions CI

---

## 🚀 Getting Started

1. Clone the repo:
   git clone https://github.com/KacperSzmyd/mood-tracker.git
   cd mood-tracker

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run the application:
    flask run

5. Access the app in your browser at http://127.0.0.1:5000


---

📂 Project structure
mood-tracker/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   ├── templates/
│   └── static/
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_mood.py
├── .github/workflows/tests.yml
├── README.md
├── requirements.txt
├── run.py
└── mood.db (created at runtime)


🧪 To Do / Upcoming Features

 Frontend improvements (JS interactivity or React)

💡 Inspiration
This project is part of a personal portfolio to demonstrate practical skills in Python, Flask, and web development.

📜 License
MIT License