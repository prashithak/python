from flask import Flask, render_template,render_template,request
import mysql.connector

user_dic={'DOC1':'123','nurse1':'789','STAFF1':'741','ADMIN':'963','PAT1':'852'}
conn=mysql.connector.connect(host='localhost',user='root',password='',database='hms')
mycursor=conn.cursor()

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('first.html')

@app.route('/lgn')
def login():
    return render_template('login.html')
@app.route('/home',methods=['POST'])
def hme():
    post=request.form['post']
    username=request.form['user']
    pwd=request.form['pwd']
    if username not in user_dic:
        return render_template('login.html',msg='invalid user')
    elif user_dic[username]!=pwd:
        return render_template('login.html',msg='invalid password')
    elif post=='DOCTOR':
        return render_template('doctor.html')
    elif post=='NURSE':
        return render_template('employee.html')
    elif post=='OTHER STAFF':
        return render_template('employee.html')
    elif post=='PATIENT':
        return render_template('register.html')
    else:
        return render_template('admin.html')

@app.route('/view',methods=['POST'])
def view():
    nam=request.form['id']
    query="SELECT * FROM patient WHERE DOC_ID="+nam
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('doctor2.html',sqldata=data)



@app.route('/read1',methods=['POST'])
def read1():
    eid=request.form['id']
    ename=request.form['name']
    post=request.form['post']
    salary=request.form['salary']
    query="INSERT INTO EMPLOYEE(EMP_ID,EMP_NAME,POST,SALARY) VALUES (%s,%s,%s,%s)"
    data=(eid,ename,post,salary)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('admin.html',msgdata='added succesfully')

@app.route('/add1')
def add1():
    return render_template('admin.html')

@app.route('/read',methods=['POST'])
def read():

    pname=request.form['name']
    gen=request.form['GEN']
    age=request.form['age']
    post=request.form['doc']
    id=request.form['id']
    query="INSERT INTO patient(p_name,gen,age,p_doc,doc_id)VALUES (%s,%s,%s,%s,%s)"
    data=(pname,gen,age,post,id)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('register.html',msgdata='added succesfully')

@app.route('/add')
def add():
    return render_template('register.html')

@app.route('/doc')
def docview():
    return render_template('doctor.html')

if __name__=='__main__':
    app.run(debug=True)