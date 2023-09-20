from cms_website import app
from flask import render_template,redirect,session,flash,request
from .data import STUDENT

@app.route("/home")
def home():
    if 'username' not in session:
        return redirect("/")
    
    for student in STUDENT:
        if student["subject"]==session["subject"]:
            student_result=student
            break
        else:
            student_result=session['subject']
 
    return render_template("home.html",student_result=student_result)