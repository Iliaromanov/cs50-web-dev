from flask import Flask, render_template
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


