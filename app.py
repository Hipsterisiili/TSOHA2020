from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    words = ["motiivi", "tilaisuus", "keinot"]
    return render_template("template1.html",message="MURHA",items=words)

@app.route("/page1")
def page1():
    return "Kokeilu"

@app.route("/test")
def test():
    content = ""
    for i in range(1,101):
        content += str(i)+" "
    return content

@app.route("/page/<int:id>")
def page(id):
    return "Tämä on sivu "+str(id) + "\n" + str(2*(id))

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html",name=request.form["name"])

