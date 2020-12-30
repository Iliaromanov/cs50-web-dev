from flask import Flask, redirect, render_template, request

app = Flask(__name__)

todos = []

@app.route("/")
def tasks():
    return render_template("tasks.html", tasks=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        new_task = request.form.get("task")
        todos.append(new_task)

        return redirect("/")