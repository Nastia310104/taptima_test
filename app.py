from flask import Flask, request, redirect, render_template
# from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#!!!Learn more about Try Exept!!!
# conn = sqlite3.connect("library.db")

# def sql_fetch(conn, command):
#     db = conn.cursor()
#     db.execute(command)
#     rows = db.fetchall()
#     return rows


#db struct:
#db.execute("""CREATE TABLE books (book_id INTEGER, name TEXT, author TEXT, 
# author_id INTEGER, description TEXT, img TEXT DEFAULT 
# "I don't know how insert images in db", year INTEGER, 
# PRIMARY KEY(book_id), FOREIGN KEY(author_id) REFERENCES authors(id))""")

# db.execute("""CREATE TABLE authors (id INTEGER, name TEXT, b_quantity INTEGER, PRIMARY KEY(id))""") 


# db = SQLAlchemy(app)

# class Books(db.Model):
#     __tablename__ = "books"
#     book_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     author = db.Column(db.Text)
#     author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
#     description = db.Column(db.Text)
#     img = db.Column(db.String(100), default="I don't know how insert images in db")
#     year = db.Column(db.Integer)

#     def __repr__(self):
#         return "<Boocks %r>" % self.id


# class Authors(db.Model):
#     __tablename__ = "authors"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     quantity = db.Column(db.Integer)

#     def __repr__(self):
#         return "<Authors %r>" % self.id

# conn = sqlite3.connect("library.db")
# db = conn.cursor()





@app.route("/", methods=["GET", "POST"])
def library():
    conn = sqlite3.connect("library.db")
    db = conn.cursor()
    # db.execute("""CREATE TABLE books (book_id INTEGER, name TEXT, author TEXT, 
    #                 author_id INTEGER, description TEXT, img TEXT DEFAULT 
    #                 "I don't know how insert images in db", year INTEGER, 
    #                 PRIMARY KEY(book_id), FOREIGN KEY(author_id) REFERENCES authors(id))""")    

    insert = ( "Фауст", "Гёте", "Лучшая книга на свете", 1000)
    db.execute("INSERT INTO books(name, author, description, year) VALUES (?, ?, ?, ?)", insert)

    db.execute("SELECT * FROM books")

    library = db.fetchall()
    
    conn.commit()

    if request.method == "POST":
        return render_template("Not yet")
    else:
        return render_template("library.html", library=library)
   

# conn.close()



if __name__ == "__main__":
    app.run(debug=True)