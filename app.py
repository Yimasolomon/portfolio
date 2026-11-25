from flask import Flask, render_template, request

app = Flask(__name__)

import sqlite3

DB_PATH =  "messages.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

def save_message(name, email, message):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message),
        )

projects = [
    {
        "title": "Deliveries",
        "description": "A delivery tracking dashboard",
        "tech": ["Python", "SQLite", "SQLAlchemy", "Alembic"],
        "link": "https://github.com/Yimasolomon/Deliveries"
    },

    {
        "title": "CampusFlow-Joe-Yima",
        "description": "CampusFlow is a Python-based helpdesk ticket management system that helps teams create, assign, track, and resolve support requests. It features ticket prioritization, status management, search and filtering, reporting, and persistent JSON storage, with input validation to maintain reliable ticket records.",
        "tech": ["Python", "JSON", "unittest", "Git", "GitHub", "CLI"],
        "link": "https://github.com/Yimasolomon/CampusFlow-Joe-Yima"
    }
]

@app.route("/")
def home():
    return render_template("home.html", name="Yima Solomon Dooga", role="AI software engineer")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    error = None
    success = False

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            error = "Please fill in all fields."
        else:
            save_message(name, email, message)
            success = True
    
    return render_template("contact.html", error=error, success=success)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

init_db()
if __name__ == "__main__":
    app.run(debug=True)
