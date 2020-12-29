import random
from flask import Flask, render_template, request

# means that flask application is being served from this file
app = Flask(__name__)

# route is what determines which web page you are on. At the end of url (eg. goole.com/maps <-- 'maps' is the route)
# '/' is the default route
@app.route("/")
def index():
    num = random.randint(1, 10)
    return render_template("index.html", num=num)

@app.route("/hello")
def hello():
    name = request.args.get("name")

    if not name:
        return render_template("failiure.html")

    return render_template("hello.html", name=name)