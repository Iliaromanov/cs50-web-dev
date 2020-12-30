from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

db = sqlite3.connect('lecture.db', check_same_thread=False)
db.row_factory = sqlite3.Row
c = db.cursor()

@app.route("/")
def index():
    c.execute("SELECT * FROM `registrants`")
    registered = c.fetchall()
    return render_template("index.html", rows=registered)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        query = """
                INSERT INTO registrants (name, email)
                VALUES (?, ?)
                """
        db.execute(query, (name, email))
        db.commit()
        return redirect("/")
