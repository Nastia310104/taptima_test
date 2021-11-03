from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Books(db.Model):
    __tablename__ = "books"
    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    description = db.Column(db.Text)
    img = db.Column(db.String(100), default="I don't know how insert images in db")
    year = db.Column(db.Integer)

    def __repr__(self):
        return "<Boocks %r>" % self.id


class Authors(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return "<Authors %r>" % self.id


@app.route("/", methods=["GET", "POST"])
def library():
    # library = 
    if request.method == "POST":
        return render_template("Not yet")
    else:
        return render_template("library.html")
        #, library=library