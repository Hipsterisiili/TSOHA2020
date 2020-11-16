from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///rasmus"
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT COUNT(*) FROM artist")
    count = result.fetchone()[0]
    result = db.session.execute("SELECT (name, id) FROM artist")
    artistit = result.fetchall()
    return render_template("index.html", count=count, artistit=artistit) 
