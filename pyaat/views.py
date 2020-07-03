from django.shortcuts import render
import pyrebase
from django.contrib import auth
from firebase_admin import db


config = {
    'apiKey': "AIzaSyAfo-l5_edC-kLXbG0b5i1l6HVyKJZ6Ej8",
    'authDomain': "eprocter-1a7aa.firebaseapp.com",
    'databaseURL': "https://eprocter-1a7aa.firebaseio.com",
    'projectId': "eprocter-1a7aa",
    'storageBucket': "eprocter-1a7aa.appspot.com",
    'messagingSenderId': "688479222669",
    'appId': "1:688479222669:web:dfeb913831a75b29c39bc4",
    'measurementId': "G-BZVH960CGZ"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()
db2 = firebase.database()
db3 = firebase.database()
db4 = firebase.database()
db5 = firebase.database()
db6 = firebase.database()
db7 = firebase.database()
db8 = firebase.database()


def index(request):
    return render(request, "pyaat/index.html")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid credentials"
        return render(request, "pyaat/index.html", {"msg": message})
    return render(request, "pyaat/basic.html")


def home(request):
    auth.logout(request)
    return render(request, "pyaat/home.html")


def studentdetails(request):
    auth.logout(request)
    return render(request, "pyaat/studdetails.html")


def studentserach(request):
    auth.logout(request)
    return render(request, "pyaat/studdisplay.html")


def studsrc(request):
    auth.logout(request)
    return render(request, "pyaat/studsrc.html")


def acasrc(request):
    auth.logout(request)
    return render(request, "pyaat/acasrc.html")


def basic(request):
    auth.logout(request)
    return render(request, "pyaat/basic.html")


def logout(request):
    auth.logout(request)
    return render(request, "pyaat/index.html")


def sem1(request):
    auth.logout(request)
    return render(request, "pyaat/1sem.html")


def sem2(request):
    auth.logout(request)
    return render(request, "pyaat/sem2.html")


def sem3(request):
    auth.logout(request)
    return render(request, "pyaat/sem3.html")


def sem4(request):
    auth.logout(request)
    return render(request, "pyaat/sem4.html")


def sem5(request):
    auth.logout(request)
    return render(request, "pyaat/sem5.html")


def sem6(request):
    auth.logout(request)
    return render(request, "pyaat/sem6.html")


def academics(request):
    auth.logout(request)
    return render(request, "pyaat/academics.html")


def signin(request):
    auth.logout(request)
    return render(request, "pyaat/signup.html")


def display(request):

    r = db.child("Procter Students").child("1BF18MCA22").child("student info").child("Gender").get().val()
    print(r)
    r2 = db.child("Users").child("details").get().val()
    print(r2)
    return render(request, "pyaat/studdisplay.html")


def register(request):
    demail = request.POST.get("semail")
    dpass = request.POST.get("spass")

    user = authe.create_user_with_email_and_password(demail, dpass)
    uid = user["localId"]
    data = {"email": demail, "status": "1"}
    db.child("Users").child(uid).child("details").set(data)
    return render(request, "pyaat/index.html")


def personal(request):
    name = request.POST.get("fname")
    lname = request.POST.get("lname")
    usn = request.POST.get("usn")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    dob = request.POST.get("dob")
    gender = request.POST.get("g")
    moj = request.POST.get("m")
    fname = request.POST.get("fathername")
    fphone = request.POST.get("fphone")
    focc = request.POST.get("foccupation")
    mname = request.POST.get("mothername")
    mphone = request.POST.get("mphone")
    mocc = request.POST.get("moccupation")
    address = request.POST.get("address")
    ec = request.POST.get("excurri")

    data = {"First Name": name, "Last Name": lname, "Email": email, "Phone": phone, "Date of Birth": dob,
            "Gender": gender, "Mod of Joining": moj, "Address": address, "Extra Curicular Activity": ec}
    d2 = {"Father Name": fname, "father phone": fphone, "FOccupation": focc, "Mother name": mname,
          "Mother phone": mphone, "moccupation": mocc}
    db.child("ProcterStudents").child(usn).child("studentinfo").child("personalinfo").set(data)
    db.child("ProcterStudents").child(usn).child("studentinfo").child("parentinfo").set(d2)

    return render(request, "pyaat/basic.html")


def dsem1(request):
    name = request.POST.get("sname")
    usn = request.POST.get("usn")
    pname = request.POST.get("pname")
    c = request.POST.get("c")
    n = request.POST.get("n")
    s = request.POST.get("s")
    total = "22"
    sub1 = "18MCA1PCUC"
    name1 = "Unix & Advanced C Programming"
    credit1 = "5"
    fname1 = request.POST.get("ucfname")
    cie1 = request.POST.get("cieuc")
    see1 = request.POST.get("seeuc")
    grade1 = request.POST.get("gradeuc")

    d1 = {"Course": name1, "credit": credit1, "faculty": fname1, "CIE": cie1, "SEE": see1, "Grade": grade1}
    db.child("Procter Students").child(usn).child("Accademic details").child("I sem").child(sub1).set(d1)

    sub2 = "18MCA1PCCO"
    name2 = "Computer Organization"
    credit2 = "3"
    fname2 = request.POST.get("cofname")
    cie2 = request.POST.get("cieco")
    see2 = request.POST.get("seeco")
    grade2 = request.POST.get("gradeco")
    d2 = {"Course": name2, "credit": credit2, "faculty": fname2, "CIE": cie2, "SEE": see2, "Grade": grade2}
    db2.child("Procter Students").child(usn).child("Accademic details").child("I sem").child(sub2).set(d2)

    sub3 = "18MCA1BSDM"
    name3 = "Discrete Mathematics"
    credit3 = "4"
    fname3 = request.POST.get("dmfname")
    cie3 = request.POST.get("ciedm")
    see3 = request.POST.get("seedm")
    grade3 = request.POST.get("gradedm")
    d3 = {"Course": name3, "credit": credit3, "faculty": fname3, "CIE": cie3, "SEE": see3, "Grade": grade3}
    db3.child("Procter Students").child(usn).child("Accademic details").child("I sem").child(sub3).set(d3)

    sub4 = "18MCA1PCWD"
    name4 = "Web Application Development"
    credit4 = "4"
    fname4 = request.POST.get("wdfname")
    cie4 = request.POST.get("ciewd")
    see4 = request.POST.get("seewd")
    grade4 = request.POST.get("gradewd")
    d4 = {"Course": name4, "credit": credit4, "faculty": fname4, "CIE": cie4, "SEE": see4, "Grade": grade4}
    db4.child("Procter Students").child(usn).child("Accademic details").child("I sem").child(sub4).set(d4)

    sub5 = "18MCA1PCOS"
    name5 = "Operating System"
    credit5 = "4"
    fname5 = request.POST.get("osfname")
    cie5 = request.POST.get("cieos")
    see5 = request.POST.get("seeos")
    grade5 = request.POST.get("gradeos")
    d5 = {"Course": name5, "credit": credit5, "faculty": fname5, "CIE": cie5, "SEE": see5, "Grade": grade5}
    db5.child("Procter Students").child(usn).child("Accademic details").child("I sem").child(sub5).set(d5)

    sub6 = "18MCA1HSPE"
    name6 = "Professional Communication and Ethics"
    credit6 = "2"
    fname6 = request.POST.get("pefname")
    cie6 = request.POST.get("ciepe")
    see6 = request.POST.get("seepe")
    grade6 = request.POST.get("gradepe")
    d6 = {"Course": name6, "credit": credit6, "faculty": fname6, "CIE": cie6, "SEE": see6, "Grade": grade6}
    db6.child("Procter Students").child(usn).child("Accademic details").child("I sem").child(sub6).set(d6)

    d = {"Total Credits":total, "No of credit earned":n, "cgpa":c, "SGPA":s}
    db8.child("Procter Students").child(usn).child("Accademic details").child("II sem").child("result").set(d)
    return render(request, "pyaat/basic.html")


def dsem2(request):
    name = request.POST.get("sname")
    usn = request.POST.get("usn")
    pname = request.POST.get("pname")
    cgpa = request.POST.get("cgpa")
    noc = request.POST.get("tcr")
    sgpa = request.POST.get("sgpa")
    total = '22'
    sub1 = "18MCA2PCOP"
    name1 = "Object Oriented Programming with C++"
    credit1 = "4"
    fname1 = request.POST.get("opfname")
    cie1 = request.POST.get("cieop")
    see1 = request.POST.get("seeop")
    grade1 = request.POST.get("gradeop")
    d1 = {"Course": name1, "credit": credit1, "faculty": fname1, "CIE": cie1, "SEE": see1, "Grade": grade1}
    db.child("Procter Students").child(usn).child("Accademic details").child("II sem").child(sub1).set(d1)

    sub2 = "18MCA2PCD"
    name2 = "Data Structures using C"
    credit2 = "4"
    gname2 = request.POST.get("dsfname")
    cie2 = request.POST.get("cieds")
    see2 = request.POST.get("seeds")
    grade2 = request.POST.get("gradeds")

    d2 = {"Course": name2, "credit": credit2, "faculty": gname2, "CIE": cie2, "SEE": see2, "Grade": grade2}
    db2.child("Procter Students").child(usn).child("Accademic details").child("II sem").child(sub2).set(d2)

    sub3 = "18MCA2PCDB"
    name3 = "Database Management System"
    credit3 = "4"
    fname3 = request.POST.get("dbfname")
    cie3 = request.POST.get("ciedb")
    see3 = request.POST.get("seedb")
    grade3 = request.POST.get("gradedb")

    sub4 = request.POST.get("e1")
    name4 = request.POST.get("ee1")
    credit4 = "4"
    fname4 = request.POST.get("elec1fname")
    cie4 = request.POST.get("cieelec1")
    see4 = request.POST.get("seeelec1")
    grade4 = request.POST.get("gradeelec1")

    sub5 = "18MCA2PCSE"
    name5 = "Software Engineering"
    credit5 = "3"
    fname5 = request.POST.get("sefname")
    cie5 = request.POST.get("ciese")
    see5 = request.POST.get("seese")
    grade5 = request.POST.get("gradese")

    sub6 = "18MCA2HSES"
    name6 = "Entrepreneurship"
    credit6 = "2"
    fname6 = request.POST.get("esfname")
    cie6 = request.POST.get("ciees")
    see6 = request.POST.get("seees")
    grade6 = request.POST.get("gradees")

    sub7 = "18MCA2SRS1"
    name7 = "Seminar -1"
    credit7 = "1"
    fname7 = request.POST.get("s1fname")
    cie7 = request.POST.get("cies1")
    see7 = request.POST.get("sees1")
    grade7 = request.POST.get("grades1")
    d3 = {"Course": name3, "credit": credit3, "faculty": fname3, "CIE": cie3, "SEE": see3, "Grade": grade3}
    db3.child("Procter Students").child(usn).child("Accademic details").child("II sem").child(sub3).set(d3)

    d4 = {"Course": name4, "credit": credit4, "faculty": fname4, "CIE": cie4, "SEE": see4, "Grade": grade4}
    db4.child("Procter Students").child(usn).child("Accademic details").child("II sem").child(sub4).set(d4)

    d5 = {"Course": name5, "credit": credit5, "faculty": fname5, "CIE": cie5, "SEE": see5, "Grade": grade5}
    db5.child("Procter Students").child(usn).child("Accademic details").child("II sem").child(sub5).set(d5)

    d6 = {"Course": name6, "credit": credit6, "faculty": fname6, "CIE": cie6, "SEE": see6, "Grade": grade6}
    db6.child("Procter Students").child(usn).child("Accademic details").child("II sem").child(sub6).set(d6)

    d7 = {"Course": name7, "credit": credit7, "faculty": fname7, "CIE": cie7, "SEE": see7, "Grade": grade7}
    db7.child("Procter Students").child(usn).child("Accademic details").child("II sem").child(sub7).set(d7)

    d = {"Total Credits": total,"No of credit earned":noc,"cgpa":cgpa,"SGPA":sgpa}
    db8.child("Procter Students").child(usn).child("Accademic details").child("II sem").child("result").set(d)
    return render(request, "pyaat/basic.html")


def dsem3(request):
    name = request.POST.get("sname")
    usn = request.POST.get("usn")
    pname = request.POST.get("pname")
    cgpa = request.POST.get("cgpa")
    noc = request.POST.get("tcr")
    sgpa = request.POST.get("sgpa")
    total = "22"
    sub1 = "18MCA3PCML"
    name1 = "Machine Learning"
    credit1 = "4"
    fname1 = request.POST.get("mlfname")
    cie1 = request.POST.get("cieml")
    see1 = request.POST.get("seeml")
    grade1 = request.POST.get("grademl")
    d1 = {"Course": name1, "credit": credit1, "faculty": fname1, "CIE": cie1, "SEE": see1, "Grade": grade1}
    db.child("Procter Students").child(usn).child("Accademic details").child("III sem").child(sub1).set(d1)
    sub2 = "18MCA3PCJP"
    name2 = "	Programming using Java"
    credit2 = "4"
    fname2 = request.POST.get("jpfname")
    cie2 = request.POST.get("ciejp")
    see2 = request.POST.get("seejp")
    grade2 = request.POST.get("gradejp")

    sub3 = "18MCA3PCNW"
    name3 = "Computer Networks"
    credit3 = "4"
    fname3 = request.POST.get("nwfname")
    cie3 = request.POST.get("cienw")
    see3 = request.POST.get("seenw")
    grade3 = request.POST.get("gradenw")

    sub4 = request.POST.get("e2")
    name4 = request.POST.get("ee2")
    credit4 = "4"
    fname4 = request.POST.get("elec2fname")
    cie4 = request.POST.get("cieelec2")
    see4 = request.POST.get("seeelec2")
    grade4 = request.POST.get("gradeelec2")

    sub5 = request.POST.get("elec3")
    name5 = request.POST.get("scelec3")
    credit5 = "3"
    fname5 = request.POST.get("elec3fname")
    cie5 = request.POST.get("cieseclec3")
    see5 = request.POST.get("seeseclec3")
    grade5 = request.POST.get("gradeseclec3")

    sub6 = "18MCA3PWM1"
    name6 = "Mini Project - I"
    credit6 = "3"
    fname6 = request.POST.get("m1fname")
    cie6 = request.POST.get("ciem1")
    see6 = request.POST.get("seem1")
    grade6 = request.POST.get("gradem1")

    sub7 = "1BMCA3NCMC"
    name7 = "MOOC Course"
    grade7 = request.POST.get("grademc")

    d7 = {"Course": name7, "Grade": grade7}
    db7.child("Procter Students").child(usn).child("Accademic details").child("III sem").child(sub7).set(d7)

    d2 = {"Course": name2, "credit": credit2, "faculty": fname2, "CIE": cie2, "SEE": see2, "Grade": grade2}
    db2.child("Procter Students").child(usn).child("Accademic details").child("III sem").child(sub2).set(d2)

    d3 = {"Course": name3, "credit": credit3, "faculty": fname3, "CIE": cie3, "SEE": see3, "Grade": grade3}
    db3.child("Procter Students").child(usn).child("Accademic details").child("III sem").child(sub3).set(d3)

    d4 = {"Course": name4, "credit": credit4, "faculty": fname4, "CIE": cie4, "SEE": see4, "Grade": grade4}
    db4.child("Procter Students").child(usn).child("Accademic details").child("III sem").child(sub4).set(d4)

    d5 = {"Course": name5, "credit": credit5, "faculty": fname5, "CIE": cie5, "SEE": see5, "Grade": grade5}
    db5.child("Procter Students").child(usn).child("Accademic details").child("III sem").child(sub5).set(d5)

    d6 = {"Course": name6, "credit": credit6, "faculty": fname6, "CIE": cie6, "SEE": see6, "Grade": grade6}
    db6.child("Procter Students").child(usn).child("Accademic details").child("III sem").child(sub6).set(d6)

    d = {"Total Credits": total,"No of credit earned":noc,"cgpa": cgpa,"SGPA":sgpa}
    db8.child("Procter Students").child(usn).child("Accademic details").child("III sem").child("result").set(d)
    return render(request, "pyaat/basic.html")


def dsem4(request):
    name = request.POST.get("sname")
    usn = request.POST.get("usn")
    pname = request.POST.get("pname")
    cgpa = request.POST.get("cgpa")
    noc = request.POST.get("n")
    sgpa = request.POST.get("sgpa")
    total = "22"

    sub1 = "18MCA4PCAD"
    name1 = "	Analysis and Design of Algorithms"
    credit1 = "3"
    fname1 = request.POST.get("adfname")
    cie1 = request.POST.get("ciead")
    see1 = request.POST.get("seead")
    grade1 = request.POST.get("gradead")
    d1 = {"Course": name1, "credit": credit1, "faculty": fname1, "CIE": cie1, "SEE": see1, "Grade": grade1}
    db.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child(sub1).set(d1)

    sub2 = "18MCA4PCAJ"
    name2 = "Advanced Java Programming"
    credit2 = "4"
    fname2 = request.POST.get("jpfname")
    cie2 = request.POST.get("ciejp")
    see2 = request.POST.get("seejp")
    grade2 = request.POST.get("gradejp")

    sub3 = "18MCA4PCPY"
    name3 = "Programming using Python"
    credit3 = "4"
    fname3 = request.POST.get("pyfname")
    cie3 = request.POST.get("ciepy")
    see3 = request.POST.get("seepy")
    grade3 = request.POST.get("gradepy")

    sub4 = request.POST.get("e4")
    name4 = request.POST.get("ee4")
    credit4 = "4"
    fname4 = request.POST.get("elec4fname")
    cie4 = request.POST.get("cieelec4")
    see4 = request.POST.get("seeelec4")
    grade4 = request.POST.get("gradeelec4")

    sub5 = request.POST.get("e5")
    name5 = name4 = request.POST.get("ee5")
    credit5 = "4"
    fname5 = request.POST.get("elec5fname")
    cie5 = request.POST.get("cieelec5")
    see5 = request.POST.get("seeelec5")
    grade5 = request.POST.get("gradeelec5")

    sub6 = "18MCA3PWM2"
    name6 = "Mini Project - II"
    credit6 = "3"
    fname6 = request.POST.get("m2fname")
    cie6 = request.POST.get("ciem2")
    see6 = request.POST.get("seem2")
    grade6 = request.POST.get("gradem2")

    sub7 = "1BMCA4NCSS"
    name7 = "Soft Skills"
    grade7 = request.POST.get("gradess")

    d7 = {"Course": name7, "Grade": grade7}
    db7.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child(sub7).set(d7)

    d2 = {"Course": name2, "credit": credit2, "faculty": fname2, "CIE": cie2, "SEE": see2, "Grade": grade2}
    db2.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child(sub2).set(d2)

    d3 = {"Course": name3, "credit": credit3, "faculty": fname3, "CIE": cie3, "SEE": see3, "Grade": grade3}
    db3.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child(sub3).set(d3)

    d4 = {"Course": name4, "credit": credit4, "faculty": fname4, "CIE": cie4, "SEE": see4, "Grade": grade4}
    db4.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child(sub4).set(d4)

    d5 = {"Course": name5, "credit": credit5, "faculty": fname5, "CIE": cie5, "SEE": see5, "Grade": grade5}
    db5.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child(sub5).set(d5)

    d6 = {"Course": name6, "credit": credit6, "faculty": fname6, "CIE": cie6, "SEE": see6, "Grade": grade6}
    db6.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child(sub6).set(d6)

    d = {"Total Credits":total,"No of credit earned":noc,"cgpa":cgpa,"SGPA":sgpa}
    db8.child("Procter Students").child(usn).child("Accademic details").child("IV sem").child("result").set(d)

    return render(request, "pyaat/basic.html")


def dsem5(request):
    name = request.POST.get("sname")
    usn = request.POST.get("usn")
    pname = request.POST.get("pname")
    cgpa = request.POST.get("cgpa")
    noc = request.POST.get("tcr")
    sgpa = request.POST.get("sgpa")
    total = "22"

    sub1 = "18MCA5HSSM"
    name1 = "Software Project Management"
    credit1 = "3"
    fname1 = request.POST.get("smfname")
    cie1 = request.POST.get("ciesm")
    see1 = request.POST.get("seesm")
    grade1 = request.POST.get("gradesm")
    d1 = {"Course": name1, "credit": credit1, "faculty": fname1, "CIE": cie1, "SEE": see1, "Grade": grade1}
    db.child("Procter Students").child(usn).child("Accademic details").child("V sem").child(sub1).set(d1)

    sub2 = "18MCA5PCWP"
    name2 = "Windows Application Programming using C#. Net"
    credit2 = "4"
    fname2 = request.POST.get("wpfname")
    cie2 = request.POST.get("ciewp")
    see2 = request.POST.get("seewp")
    grade2 = request.POST.get("gradewp")

    sub3 = "18MCA5PCMU"
    name3 = "Modeling with UML"
    credit3 = "3"
    fname3 = request.POST.get("mufname")
    cie3 = request.POST.get("ciemu")
    see3 = request.POST.get("seemu")
    grade3 = request.POST.get("grademu")

    sub4 = request.POST.get("e6")
    name4 = request.POST.get("ee6")
    credit4 = "4"
    fname4 = request.POST.get("elec6fname")
    cie4 = request.POST.get("cieelec6")
    see4 = request.POST.get("seeelec6")
    grade4 = request.POST.get("gradeelec6")

    sub5 = request.POST.get("e7")
    name5 = request.POST.get("ee7")
    credit5 = "4"
    fname5 = request.POST.get("elec7fname")
    cie5 = request.POST.get("cieelec7")
    see5 = request.POST.get("seeelec7")
    grade5 = request.POST.get("gradeelec7")

    sub6 = "18MCA5PWM3"
    name6 = "Mini Project - III"
    credit6 = "2"
    fname6 = request.POST.get("m3fname")
    cie6 = request.POST.get("ciem3")
    see6 = request.POST.get("seem3")
    grade6 = request.POST.get("gradem3")

    sub7 = "18MCA5SRS2"
    name7 = "Seminar 2"
    credit7 = "2"
    fname7 = request.POST.get("s2fname")
    cie7 = request.POST.get("cies2")
    see7 = request.POST.get("sees2")
    grade7 = request.POST.get("grades2")

    d7 = {"Course": name7, "credit": credit7, "faculty": fname7, "CIE": cie7, "SEE": see7, "Grade": grade7}
    db7.child("Procter Students").child(usn).child("Accademic details").child("V sem").child(sub7).set(d7)

    d2 = {"Course": name2, "credit": credit2, "faculty": fname2, "CIE": cie2, "SEE": see2, "Grade": grade2}
    db2.child("Procter Students").child(usn).child("Accademic details").child("V sem").child(sub2).set(d2)

    d3 = {"Course": name3, "credit": credit3, "faculty": fname3, "CIE": cie3, "SEE": see3, "Grade": grade3}
    db3.child("Procter Students").child(usn).child("Accademic details").child("V sem").child(sub3).set(d3)

    d4 = {"Course": name4, "credit": credit4, "faculty": fname4, "CIE": cie4, "SEE": see4, "Grade": grade4}
    db4.child("Procter Students").child(usn).child("Accademic details").child("V sem").child(sub4).set(d4)

    d5 = {"Course": name5, "credit": credit5, "faculty": fname5, "CIE": cie5, "SEE": see5, "Grade": grade5}
    db5.child("Procter Students").child(usn).child("Accademic details").child("V sem").child(sub5).set(d5)

    d6 = {"Course": name6, "credit": credit6, "faculty": fname6, "CIE": cie6, "SEE": see6, "Grade": grade6}
    db6.child("Procter Students").child(usn).child("Accademic details").child("V sem").child(sub6).set(d6)

    d = {"Total Credits":total,"No of credit earned":noc,"cgpa":cgpa,"SGPA":sgpa}
    db8.child("Procter Students").child(usn).child("Accademic details").child("V sem").child("result").set(d)

    return render(request, "pyaat/basic.html")


def dsem6(request):
    name = request.POST.get("sname")
    usn = request.POST.get("usn")
    pname = request.POST.get("pname")
    cgpa = request.POST.get("cgpa")
    noc = request.POST.get("tcr")
    sgpa = request.POST.get("sgpa")
    total = "22"

    sub1 = "18MCA6NTI1"
    name1 = "Internship 1"
    credit1 = "2"
    fname1 = request.POST.get("t1fname")
    cie1 = request.POST.get("ciet1")
    see1 = request.POST.get("seet1")
    grade1 = request.POST.get("gradet1")

    sub2 = "18MCA6NTI2"
    name2 = "Internship 2"
    credit2 = "2"
    fname2 = request.POST.get("t2fname")
    cie2 = request.POST.get("ciet2")
    see2 = request.POST.get("seet2")
    grade2 = request.POST.get("gradet2")

    sub3 = "18MCA6PWMP"
    name3 = "Major Project"
    credit3 = "16"
    fname3 = request.POST.get("mpfname")
    cie3 = request.POST.get("ciemp")
    see3 = request.POST.get("seemp")
    grade3 = request.POST.get("grademp")

    sub4 = "18MCA6HSPR"
    name4 = "Cyber Regulations and IPR"
    credit4 = "2"
    fname4 = request.POST.get("prfname")
    cie4 = request.POST.get("ciepr")
    see4 = request.POST.get("seepr")
    grade4 = request.POST.get("gradepr")

    d1 = {"Course": name1, "credit": credit1, "faculty": fname1, "CIE": cie1, "SEE": see1, "Grade": grade1}
    db2.child("Procter Students").child(usn).child("Accademic details").child("VI sem").child(sub1).set(d1)

    d2 = {"Course": name2, "credit": credit2, "faculty": fname2, "CIE": cie2, "SEE": see2, "Grade": grade2}
    db3.child("Procter Students").child(usn).child("Accademic details").child("VI sem").child(sub2).set(d2)

    d3 = {"Course": name3, "credit": credit3, "faculty": fname3, "CIE": cie3, "SEE": see3, "Grade": grade3}
    db4.child("Procter Students").child(usn).child("Accademic details").child("VI sem").child(sub3).set(d3)

    d4 = {"Course": name4, "credit": credit4, "faculty": fname4, "CIE": cie4, "SEE": see4, "Grade": grade4}
    db5.child("Procter Students").child(usn).child("Accademic details").child("VI sem").child(sub4).set(d4)

    d = {"Total Credits":total,"No of credit earned":noc,"cgpa":cgpa,"SGPA":sgpa}
    db8.child("Procter Students").child(usn).child("Accademic details").child("VI sem").child("result").set(d)
    return render(request, "pyaat/basic.html")
