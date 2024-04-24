import base64
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, render_template, request, session, redirect, jsonify
from DBConnection import Db
import time

app = Flask(__name__)
app.secret_key="hi"

static_path=r"C:\Users\Admin\Music\web\web\static\\"



@app.route('/')
def hello_world():
    return render_template("login_temp.html")
@app.route("/login_post", methods=['post'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    res=db.selectOne("SELECT * FROM login WHERE username='"+username+"' AND PASSWORD='"+password+"'")
    if res is not None:
        session['lid']=res['login_id']
        if res['user_type']=="admin":
            session['lg']="yes"
            return redirect("/admin_home")
        elif res['user_type']=="parent":
            db=Db()
            res2=db.selectOne("select * from parent where parent_id='"+str(res['login_id'])+"'")
            session['lg']="yes"
            session['uname']=res2['name']
            return redirect("/parent_home")
        else:
            return "<script>alert('Unauthorised user');window.location='/';</script>"
    else:
        return "<script>alert('Invalid Details');window.location='/';</script>"


@app.route("/logout")
def logout():
    session['lg']=""
    return "<script>alert('Logged out');window.location='/';</script>"


###################         ADMIN
@app.route("/admin_home")
def admin_home():
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    return render_template("admin/admin_index.html")
    # return render_template("admin/home.html")

@app.route("/admin_add_object")
def admin_add_object():
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    return render_template("admin/add_object.html")

@app.route("/admin_add_object_post", methods=['post'])
def admin_add_object_post():
    objname=request.form['textfield']
    img=request.files['filefield']
    dt=time.strftime("%Y%m%d_%H%M%S")
    img.save(static_path+"objects\\" + dt + ".jpg")
    path="/static/objects/" + dt + ".jpg"
    db=Db()
    db.insert("INSERT INTO object(object_name, image) VALUES('"+objname+"', '"+path+"')")
    return "<script>alert('Object Added');window.location='/admin_add_object';</script>"


@app.route("/admin_view_object")
def admin_view_object():
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    db=Db()
    res=db.select("SELECT * FROM `object`")
    return render_template("admin/view_objects.html", data=res)

@app.route("/admin_delete_object/<oid>")
def admin_delete_object(oid):
    db=Db()
    db.delete("DELETE FROM object WHERE object_id='"+oid+"'")
    return redirect("/admin_view_object")


@app.route("/admin_add_puzzle")
def admin_add_puzzle():
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    return render_template("admin/add_puzzle.html")

@app.route("/admin_add_puzzle_post", methods=['post'])
def admin_add_puzzle_post():
    objname=request.form['textfield']
    img=request.files['filefield']
    dt=time.strftime("%Y%m%d_%H%M%S")
    img.save(static_path+"puzzle\\" + dt + ".jpg")
    path="/static/puzzle/" + dt + ".jpg"
    db=Db()
    db.insert("INSERT INTO puzzle(puzzle_name, DATE, image) VALUES('"+objname+"', curdate(), '"+path+"')")
    return "<script>alert('Puzzle Added');window.location='/admin_add_puzzle';</script>"


@app.route("/admin_view_puzzle")
def admin_view_puzzle():
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    db=Db()
    res=db.select("SELECT * FROM `puzzle`")
    return render_template("admin/view_puzzle.html", data=res)

@app.route("/admin_delete_puzzle/<pid>")
def admin_delete_puzzle(pid):
    db=Db()
    db.delete("DELETE FROM puzzle WHERE puzzle_id='"+pid+"'")
    return redirect("/admin_view_puzzle")

@app.route("/admin_view_complaints")
def admin_view_complaints():
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    db=Db()
    res=db.select("select * from complaint, parent where complaint.parent_id=parent.parent_id and complaint.reply='pending'")
    return render_template("admin/view_complaints.html", data=res)

@app.route("/send_reply/<id>")
def send_reply(id):
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    return render_template("admin/send_reply.html", id=id)

@app.route("/send_reply_post", methods=['post'])
def send_reply_post():
    id=request.form['hid']
    reply=request.form['textarea']
    db=Db()
    db.update("update complaint set reply='"+reply+"' where complaint_id='"+id+"'")
    return "<script>alert('Reply sent');window.location='/admin_view_complaints';</script>"

@app.route("/admin_view_parents")
def admin_view_parents():
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    db=Db()
    res=db.select("select * from parent")
    return render_template("admin/view_parents.html", data=res)

@app.route("/admin_view_students/<pid>")
def admin_view_students(pid):
    if session['lg']!='yes':
        return "<script>alert('You are logged out');window.location='/';</script>"
    db=Db()
    res=db.select("SELECT * FROM `student` WHERE parent_id='"+pid+"'")
    return render_template("admin/view_students.html", data=res)




#################       PARENT
@app.route("/register")
def register():
    return render_template("reg_temp.html")
@app.route("/register_post", methods=['post'])
def register_post():
    name=request.form['Name']
    email=request.form['Email']
    phone=request.form['Phone']
    house=request.form['House']
    place=request.form['Place']
    city=request.form['City']
    state=request.form['State']
    img=request.files['Image']
    pswd=request.form['Password']
    db=Db()
    lid=db.insert("INSERT INTO login(username, PASSWORD, user_type) VALUES('"+email+"', '"+pswd+"', 'parent')")
    dt=time.strftime("%Y%m%d_%H%M%S")
    img.save(static_path + "parent\\" + dt + ".jpg")
    path="/static/parent/" + dt + ".jpg"
    db.insert("INSERT INTO parent VALUES('"+str(lid)+"','"+name+"', '"+email+"', '"+phone+"', '"+path+"', '"+house+"' ,'"+place+"' ,'"+city+"' ,'"+state+"')")
    return "<script>alert('Registered');window.location='/';</script>"


@app.route("/parent_home")
def parent_home():
    return render_template("parent/parent_index.html")

@app.route("/parent_view_profile")
def parent_view_profile():
    db=Db()
    res=db.selectOne("SELECT * FROM parent WHERE parent_id='"+str(session['lid'])+"'")
    return render_template("parent/view_profile.html", data=res)

@app.route("/parent_add_child")
def parent_add_child():
    return render_template("parent/add_child.html")

@app.route("/parent_add_child_post", methods=['post'])
def parent_add_child_post():
    name=request.form['textfield']
    email=request.form['textfield2']
    age=request.form['textfield3']
    gender=request.form['radio']
    password=random.randint(1000, 9999)
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("dysl9050@gmail.com", "przejxgxvziogubh")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "dysl9050@gmail.com"
    msg['To'] = email
    msg['Subject'] = "E Learning password"
    body = "Password for your child " + name + " is " + str(password)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)

    db=Db()
    lid=db.insert("INSERT INTO login(username, PASSWORD, user_type) VALUES('"+email+"', '"+str(password)+"', 'student')")
    db.insert("INSERT INTO student(student_id, NAME, email, age, gender, parent_id) VALUES('"+str(lid)+"', '"+name+"', '"+email+"', '"+age+"', '"+gender+"', '"+str(session['lid'])+"')")
    return "<script>alert('Child added');window.location='/parent_add_child';</script>"

@app.route("/parent_view_child")
def parent_view_child():
    db=Db()
    res=db.select("select * from student where parent_id='"+str(session['lid'])+"'")
    return render_template("parent/view_child.html", data=res)

@app.route("/parent_delete_child/<cid>")
def parent_delete_child(cid):
    db=Db()
    db.delete("delete from student where student_id='"+cid+"'")
    return redirect("/parent_view_child")

@app.route("/parent_view_progress/<id>")
def parent_view_progress(id):
    db=Db()
    res=db.select("SELECT * FROM `result` WHERE student_id='"+str(id)+"'")
    norm_count=0
    dis_count=0
    tot=len(res)
    for i in res:
        if i['prediction'] == "Dyslexic":
            dis_count+=1
        else:
            norm_count+=1
    if tot != 0:
        dis_perc=round(dis_count * 100/tot, 2)
        norm_perc=round(norm_count * 100/tot, 2)
    else:
        dis_perc=0
        norm_perc=0
    return render_template("parent/view_progress.html", data=res, norm_count=norm_count, norm_perc=norm_perc, dis_count=dis_count,dis_perc=dis_perc, tot=tot)

@app.route("/parent_add_person")
def parent_add_person():
    return render_template("parent/add_familiar_person.html")

@app.route("/parent_add_person_post", methods=['post'])
def parent_add_person_post():
    name=request.form['textfield']
    relation=request.form['textfield2']
    img=request.files['filefield']
    dt=time.strftime("%Y%m%d_%H%M%S")
    img.save(static_path + "person\\" + dt + ".jpg")
    path="/static/person/" + dt + ".jpg"
    db=Db()
    db.insert("INSERT INTO `familiar_person`(parent_id, NAME, relation, image) VALUES('"+str(session['lid'])+"', '"+name+"', '"+relation+"', '"+path+"')")
    return "<script>alert('Person added');window.location='/parent_add_person';</script>"


@app.route("/parent_view_person")
def parent_view_person():
    db=Db()
    res=db.select("select * from familiar_person where parent_id='"+str(session['lid'])+"'")
    return render_template("parent/view_person.html", data=res)

@app.route("/parent_delete_person/<pid>")
def parent_delete_person(pid):
    db=Db()
    db.delete("delete from familiar_person where person_id='"+pid+"'")
    return redirect("/parent_view_person")

@app.route("/send_complaint")
def send_complaint():
    return render_template("parent/send_complaint.html")

@app.route("/send_complaint_post", methods=['post'])
def send_complaint_post():
    comp=request.form['textfield']
    db=Db()
    db.insert("INSERT INTO `complaint`(parent_id, DATE, complaint, reply) VALUES('"+str(session['lid'])+"', CURDATE(), '"+comp+"', 'pending')")
    return "<script>alert('Complaint sent');window.location='/send_complaint';</script>"

@app.route("/parent_view_replies")
def parent_view_replies():
    db=Db()
    res=db.select("SELECT * FROM complaint WHERE parent_id='"+str(session['lid'])+"'")
    return render_template("parent/view_reply.html", data=res)

@app.route("/parent_delete_complaint/<cid>")
def parent_delete_complaint(cid):
    db=Db()
    db.delete("delete from complaint where complaint_id='"+cid+"'")
    return redirect("/parent_view_replies")

###################################                 ANDROID
@app.route("/and_login", methods=['post'])
def and_login():
    username=request.form['username']
    password=request.form['password']
    db=Db()
    res=db.selectOne("SELECT * FROM login WHERE username='"+username+"' AND PASSWORD='"+password+"'")
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok", type=res['user_type'], lid=res['login_id'])

@app.route("/and_profile", methods=['post'])
def and_profile():
    lid=request.form['lid']
    db=Db()
    res=db.selectOne("select * from student where student_id='"+lid+"'")
    return jsonify(status="ok", data=res)

@app.route("/and_view_alphabets", methods=['post'])
def and_view_alphabets():
    alph=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z"]
    res=[]
    for i in alph:
        res.append({"alph" : i, "path": "/static/alphabets/" + i + ".jpg"})
    return jsonify(status="ok", data=res)

@app.route("/and_load_alphabets", methods=['post'])
def and_load_alphabets():
    pos=request.form['pos']
    print("PP ", pos)
    alph=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z"]
    res=[]
    res2=[]
    res2.append(alph[int(pos)])
    while len(res2)<4:
        ch=random.choice(alph)
        if ch not in res2:
            res2.append(ch)
    print("Choices before :", res2)
    random.shuffle(res2)
    print("Choices after : ", res2)
    for i in alph:
        res.append({"alph" : i, "path": "/static/alphabets/" + i + ".jpg"})
    return jsonify(status="ok", data=res, op1=res2[0], op2=res2[1], op3=res2[2], op4=res2[3])


@app.route("/and_check_alph", methods=['post'])
def and_load_alphabet():
    pos=request.form['pos']
    ans=request.form['ans']
    alph=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z"]
    res=[]
    for i in alph:
        res.append({"alph" : i, "path": "/static/alphabets/" + i + ".jpg"})
    return jsonify(status="ok", data=res)

@app.route("/insert_test_marks", methods=['post'])
def insert_test_marks():
    lid=request.form['lid']
    correct=request.form['correct']
    attended=request.form['attended']
    type=request.form['type']
    perc = int(correct) * 100 / int(attended)
    if perc < 30:
        stat = "Dyslexic"
    else:
        stat = "Normal"
    db=Db()
    res=db.selectOne("select * from result where date=curdate() and student_id='"+lid+"' and test_type='"+type+"'")
    if res is None:
        db=Db()
        db.insert("INSERT INTO result(DATE, student_id, test_type, correct, attended, prediction) "
                  "VALUES(CURDATE(), '"+lid+"', '"+type+"', '"+correct+"', '"+attended+"', '"+stat+"')")
    else:
        db=Db()
        db.update("update result set correct='"+correct+"', attended='"+attended+"', prediction='"+stat+"' where result_id='"+str(res['result_id'])+"'")

    return jsonify(status="ok", stat="stat")


@app.route("/and_view_objects", methods=['post'])
def and_view_objects():
    objs=["ant", "ball", "car", "dog", "egg", "fish", "goat", "horse", "ice", "jam", "key", "lemon", "mushroom",
          "nest", "owl", "pig", "queen", "rocket", "snake", "turtle", "umbrella", "violin", "whale", "xylophone",
          "yacht", "zebra"]
    res=[]
    for i in objs:
        res.append({"obj" : i, "path": "/static/alphabets/" + i + ".jpg"})
    return jsonify(status="ok", data=res)

@app.route("/and_check_obj", methods=['post'])
def and_check_obj():
    pos=request.form['pos']
    ans=request.form['ans']
    objs=["ant", "ball", "car", "dog", "egg", "fish", "goat", "horse", "ice", "jam", "key", "lemon", "mushroom",
          "nest", "owl", "pig", "queen", "rocket", "snake", "turtle", "umbrella", "violin", "whale", "xylophone",
          "yacht", "zebra"]
    pos=int(pos)
    if ans == objs[pos] or ans.lower() == objs[pos]:
        return jsonify(status="ok")
    else:
        return jsonify(status="no")


@app.route("/and_load_rhyming", methods=['post'])
def and_load_rhyming():
    pos=request.form['pos']
    print("PP ", pos)
    word1=["bat", "cap", "hen", "jet", "fin", "cot", "cow", "fog", "god", "ball", "stab", "trip", "crop"]
    word2=["cat", "map", "ten", "net", "kin", "pot", "now", "log", "nod", "wall", "crab", "grip", "drop"]
    res=[]
    res2=[]
    res2.append(word2[int(pos)])
    while len(res2)<4:
        ch=random.choice(word2)
        if ch not in res2:
            res2.append(ch)
    print("Choices before :", res2)
    random.shuffle(res2)
    print("Choices after : ", res2)
    for i in range(len(word1)):
        res.append({"word" : word1[i], "rhyming": word2[i]})
    return jsonify(status="ok", data=res, op1=res2[0], op2=res2[1], op3=res2[2], op4=res2[3])

@app.route("/and_load_hand", methods=['post'])
def and_load_hand():
    alph=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
          "S", "T", "U", "V", "W", "X", "Y", "Z"]
    aa=random.choice(alph)
    return jsonify(status="ok", alph=aa)

from predict import predictcnn
@app.route("/and_upload_handwriting", methods=['post'])
def and_upload_handwriting():
    lid=request.form['lid']
    pic=request.form['attach']
    a = base64.b64decode(pic)
    fh = open(static_path +"a.jpg", "wb")
    fh.write(a)
    fh.close()
    label_list = ["Dyslexic", "Normal"]
    pred = predictcnn(static_path +"a.jpg")
    print("Folder index : ", pred)
    idx = pred[0]
    val= label_list[idx]
    print("Prediction : ", val)
    db=Db()
    res=db.selectOne("select * from result where date=curdate() and student_id='"+lid+"' and test_type='Handwriting'")
    if res is None:
        db=Db()
        db.insert("INSERT INTO result(DATE, student_id, test_type, prediction) "
                  "VALUES(CURDATE(), '"+lid+"', 'Handwriting',  '"+val+"')")
    else:
        db=Db()
        db.update("update result set prediction='"+val+"' where result_id='"+str(res['result_id'])+"'")

    return jsonify(status="ok", pred=val)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
#
#
# dysl9050@gmail.com
# Dyslexia@2k24
# xrdd vlot bfcn wnat