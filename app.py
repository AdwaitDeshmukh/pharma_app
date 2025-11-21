from flask import Flask, request, redirect, render_template
from utils.db import init_db, get_db
from datetime import datetime


app = Flask(__name__)

# Initialize DB on start
init_db()

@app.route("/")
def home():
    return render_template("login_page.html")

@app.route("/login_validation", methods=["POST"])
def login_validation():
    username = request.form.get("username")
    password = request.form.get("password")
    
    conn = get_db()
    cursor = conn.cursor()

    # Check user in database
    user = cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()

    if user:
        return render_template("dashboard.html")
    else:
        return redirect("/")
    
@app.route("/master-entry")
def master_entry():
    return render_template("master-entry.html")

if __name__ == "__main__":
    app.run(debug=True)
