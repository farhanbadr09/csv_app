from logging import Logger

try:
    import os
    import sqlite3
    from flask import Flask, render_template, request, redirect, url_for, jsonify, json, flash, send_file,flash
    # from flask_sqlalchemy import SQLAlchemy
    # from sqlalchemy import and_
    # from sqlalchemy import or_
    from click import File
    import csv
    import psycopg2
    import psycopg2.extras

    print("found")
except:
    print("not found d")

myApp = Flask(__name__)
myApp.secret_key = os.urandom(24)


project_dir = os.path.abspath(os.path.dirname(__file__))
print("=" * 100)

a=[]
c2=[]
c=[]
@myApp.route('/csv')
def csv():
    conn = sqlite3.connect("data.sqlite")
    cor = conn.cursor()  
    record=[]
    for row in cor.execute('SELECT _name FROM  _flight'):
        row=str(row).replace("('","")
        row=str(row).replace("',)","")
        record.append(row)
        

    return render_template("farhan.html",record=record)

@myApp.route('/uploadcsv',methods=['GET', 'POST'])
def uploadcsv():
    csvfile= request.files["csv"]
    target_img = os.path.join(project_dir, 'static/csv')
    if not os.path.isdir(target_img):
        os.mkdir(target_img)
    destination1 = "/".join([target_img, csvfile.filename])
    csvfile.save(destination1)
    fil=open('static/csv/'+ csvfile.filename,"r")
    fil=fil.readlines()
    global a
    global c2
    global c
  

    for i in fil:
        a.append(i.split(","))

    print(a[0])
    count=0
    count2=0
    for i in range(int(len(a[0]))):
        c.append(count)
        count=count+1
    for i in range(int(len(a))):
        c2.append(count2)
        count2=count2+1
    print(count)
    print(count2)
    conn = sqlite3.connect("data.sqlite")
    cor = conn.cursor()  
    record=[]
    for row in cor.execute('SELECT _name FROM  _flight'):
        row=str(row).replace("('","")
        row=str(row).replace("',)","")
        record.append(row)
    return render_template("farhan.html",record=record,c=c,a=a,c2=c2)

@myApp.route('/uploadflight',methods=['GET', 'POST'])
def uploadflight():
    conn = sqlite3.connect("data.sqlite")
    cor = conn.cursor() 
    record=[]
    for row in cor.execute('SELECT _name FROM  _flight'):
        row=str(row).replace("('","")
        row=str(row).replace("',)","")
        record.append(row)
    flight= request.form["flight"]
    MAWB = request.form["MAWB"]
    EAT= request.form["EAT"]
    remarks= request.form["Remarks"]
    cor.execute("INSERT INTO Record (flight_name,MAWB,EAT,remarks) VALUES (?,?,?,?)",(flight,MAWB,EAT,remarks))
    conn.commit()
    # conn = sqlite3.connect("data.sqlite")
    # cor = conn.cursor()  
    flash('Added successfully', 'success')
  
    return render_template("farhan.html",record=record,c=c,a=a,c2=c2)




if __name__ == "__main__":
    myApp.run(debug=True)
