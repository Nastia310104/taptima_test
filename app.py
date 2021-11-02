from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def library():
    # library = db.execute
    if request.method == "POST":
        return render_template("Not yet")
    else:
        return render_template("library.html")
        #, library=library