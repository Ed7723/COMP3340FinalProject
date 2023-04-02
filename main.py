from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title = 'Homepage')

@app.route("/create")
def create():
    return render_template("create.html", title = 'Create Items')

@app.route("/view")
def view():
    return render_template("view.html", title = 'View Items')