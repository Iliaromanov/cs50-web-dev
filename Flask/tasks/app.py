from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def tasks():
    return "1"

@app.route("/add")
def add():
    return "2"