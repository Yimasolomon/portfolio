from flask import Flask, render_template, request

app = Flask(__name__)

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
            print(f"New message from {name} ({email}): {message}")
            success = True
    
    return render_template("contact.html", success=success)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
