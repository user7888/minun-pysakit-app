from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Address for database:
# use 'postgresql' or 'postgresql+psycopg2'
# and username.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2:///edjunno"
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT content FROM messages")
    messages = result.fetchall()
    return render_template("index_db.html", count=len(messages), messages=messages) 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO messages (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")