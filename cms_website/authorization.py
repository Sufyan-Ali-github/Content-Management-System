from cms_website import app
from flask import render_template,redirect,session,flash,request,url_for
from .data import TEACHER
from .index import *

@app.route("/login",methods=['GET','POST'])
def login():
    
    if 'username'  in session:
     return redirect("/home")
    if request.method=='POST':
        user_creds=request.form.to_dict()

        username_found=False
        for user in TEACHER:
            if user["username"]==user_creds["username"]:
                username_found=True
                if user["password"]==user_creds["password"]:
                  session['username']=user['username']
                  session['img']=user['img']
                  session["subject"]=user["subject"]
                  return redirect("/home")
                else:
                   flash("Invalid password")
                   return redirect("/")
        if not username_found:
          flash("Username doesn't exist")
          return redirect("/")
    return render_template("index.html")



@app.route("/register",methods=['GET','POST'])
def register():
   
   if 'username' in session:
      return redirect("/home")
   if request.method=='POST':
      data=request.form.to_dict()
      if data['password'] != data['c_password']:
         flash("Password didn't Match")
         return redirect("/register")
      
      for user in TEACHER:
         if user['username'] == data['username']:
            flash("Username already exist")
            return redirect("/register")
         TEACHER.append({
            "username": data['username'],
            "password": data['password'],
            "subject": data['subject'],
            "img": data['image']
         })
         flash("Account created successfully")
         return redirect("/")
      
 
   return render_template("register.html")



@app.route("/logout")
def logout():
   if 'username' in session:
      session.pop('username')
      return redirect("/")