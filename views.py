from hello import app
from flask import render_template

@app.route("/")
def hello_world():
    return render_template("homepage.html")


@app.route("/blog")
def blog():
    return "<p>bem vindo ao blog!<p>"
