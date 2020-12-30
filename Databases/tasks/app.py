from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# session is a dictionary
# a session is individual for each user

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/")
def tasks():
    if "todos" not in session:
        session["todos"] = []
    return render_template("tasks.html", tasks=session["todos"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        new_task = request.form.get("task")
        session["todos"].append(new_task)

        return redirect("/")