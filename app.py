from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Deliveries",
        "description": "A delivery tracking dashboard",
        "tech": ["python", "SQLite", "Alchemy", "Alembic"],
        "link": "https://github.com/Yimasolomon/Deliveries"
    }
]

@app.route("/")
def home():
    return render_template("home.html", name="Yima Solomon Dooga", role="AI software engineer")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
