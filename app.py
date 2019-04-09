from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/") 
@app.route("/home") 
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title="About")