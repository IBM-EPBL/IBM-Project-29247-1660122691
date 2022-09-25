from crypt import methods
from flask import Flask, render_template, request, redirect, session,url_for
import sqlite3 as sql
import sys
app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'




@app.route('/adduser')
def new_student():
   return render_template('signup.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   print('addrec')
   if request.method == 'POST':
      try:
         name = request.form['name']
         email = request.form['email']
         roll = request.form['roll']
         pw = request.form['pass']
         with sql.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO student (email,username,rollnumber,password) VALUES (?,?,?,?)",(name,email,roll,pw) )
            con.commit()
           
      except:
         con.rollback()
        
      
      finally:
         return redirect (url_for('signin'))
         con.close()

@app.route('/signin')
def signin():
    print("d")
    return render_template ('signin.html')


@app.route('/login',methods=["POST"])
def login():
    if(request.method == "POST"):
        try:
            password = request.form['pass']
            email = request.form['email']
            with sql.connect("student.db") as con:
             cur = con.cursor()
             query = 'select * from student where username = "'+email+'" and password = '+password+''
             cur.execute(query)
             students = cur.fetchall()
             if(len(students)==0):
                print("no")
                
             else:
               
               return render_template("welcome.html")
             
        except:
            con.rollback()
            print (sys.exc_info()[0])
        
    
     
if __name__ == '__main__':
   app.run(debug = True)