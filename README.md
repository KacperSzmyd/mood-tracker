# Mood Tracker Web App

A simple web application for tracking your daily mood. Built with Flask, SQLite, and basic HTML/CSS. The app allows users to submit their mood each day and view their mood history.

## 🔧 Technologies Used

- Python 3.x
- Flask
- SQLite + SQLAlchemy
- HTML / CSS (optional JS)
- (Optional) GitHub Actions for CI/CD
- (Optional) Render or Railway for deployment

## ✨ Features

- Submit your current mood through a web form
- Save entries to a local SQLite database
- View a list of past mood entries with timestamps
- Simple, clean UI
- Modular code structure with blueprints and models

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
    flask --app run run

5. Access the app in your browser at http://127.0.0.1:5000


🧪 To Do / Upcoming Features

 Export mood history (CSV)

 Graph visualization of moods

 Tests and CI integration

 Frontend improvements (JS interactivity or React)

💡 Inspiration
This project is part of a personal portfolio to demonstrate practical skills in Python, Flask, and web development.

📜 License
MIT License