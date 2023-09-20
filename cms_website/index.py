from cms_website import app
from flask import render_template
from .authorization import *

@app.route("/")
def index():
    if 'username' in session:
        return redirect("/home")
    
    return render_template("index.html")