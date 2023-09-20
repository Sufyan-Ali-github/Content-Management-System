from cms_website import app
from flask import render_template,redirect,session,flash,request,url_for
from .data import STUDENT


@app.route("/edit_record/<Sr_no>",methods=['GET','POST'])
def edit(Sr_no):
    if 'username' not in session:
        return redirect("/")
    
    for student in STUDENT:
       if student["subject"]==session["subject"]:
           student_edit=student
           break
       


    if request.method=="POST":
        data=request.form.to_dict(flat=True)
        session["roll_no"]=data["roll_no"]
        for stnd in STUDENT:
            if stnd["subject"].upper()==session["subject"].upper():
                update_student=stnd
                break

        for std in update_student["student_info"]:
                 if std["roll_no"]==session["roll_no"]:
                    std["roll_no"]=data["roll_no"]
                    std["name"]=data["name"]
                    std["father_name"]=data["father_name"]
                    std["class"]=data["class"]
                    std['dob']=data['dob']
                    std['gender']=data['gender']
                    std['email']=data['email']
                    std['contact']=data['contact']
                    std['address']=data['address']
                    std["mid_marks"]=data["mid_terms"]
                    std["final_marks"]=data["final_marks"]
                    std["obtain_marks"]=data["obtain_marks"]
                    std["Total marks"]=data["full_marks"]
                    break
        flash("Updated the Record")    
        return redirect("/home")
    
    return render_template("edit.html",student_edit=student_edit,Sr_no=Sr_no)



@app.route("/view_record/<sr_no>")
def view(sr_no):
    if 'username' not in session:
        return redirect("/")

    for student in STUDENT:
       if student["subject"]==session["subject"]:
           student_record=student
           break
       
    return render_template("view.html",student_record=student_record,sr_no=sr_no)


@app.route("/delete_record/<sr_no>")
def delete(sr_no):
    if 'username' not in session:
        return redirect("/")
    for stn in STUDENT:
            if stn["subject"].upper()==session["subject"].upper():
                delete_student=stn
                break

    for st in delete_student["student_info"]:
        if st["sr"]==sr_no:
            st['img']=' '
            st['father_name']=' '
            st['name']=' '
            st['roll_no']=' '
            st['class']=' '
            st['mid_marks']=' '
            st['final_marks']=' '
            st['obtain_marks']=' '
            st['Total marks']=' '
            st['dob']=' '
            st['contact']=' '
            st['gender']=' '
            st['address']=' '
            st['email']=' '
            flash("Delete the record")
            return redirect("/home")

    
    return render_template("home.html")



