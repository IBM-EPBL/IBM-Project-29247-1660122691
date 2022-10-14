from crypt import methods
from flask import Flask, render_template, request, redirect, session,url_for
import sqlite3 as sql
import sys
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qhm97791;PWD=JGcXM9H6DJ38AEZJ;",'','')

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
         sql = "INSERT into user values ('{}', '{}','{}', '{}')".format(email, name, roll, pw)
         stmt = ibm_db.exec_immediate(conn, sql)
         
     
      except:
        print ("addrec",sys.exc_info()[0])
        
      
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
         mail = request.form['email']
         pwd = request.form['pass']
         sql = "SELECT * from user where email = '{}'".format(mail)
        
         stmt = ibm_db.exec_immediate(conn, sql)
         dict = ibm_db.fetch_assoc(stmt)         
         if (mail == dict['EMAIL'].strip() and pwd == dict['PASSWORD'].strip()):
            # print("if clause")
            return render_template("welcome.html", user=dict['NAME'])
         else:
            return render_template("signin.html",message = "Not a valid user")
    
             
        except:            
            print ("login",sys.exc_info()[0])
      return render_template("signin.html",message = "Not a valid user")
        
   #  return render_template('signin.html')
     
if __name__ == '__main__':
   app.run(debug = True)