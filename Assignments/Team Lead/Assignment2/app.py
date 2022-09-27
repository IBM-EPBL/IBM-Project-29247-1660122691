from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'


@app.route('/')
def home():
   return render_template('signin.html')

@app.route('/signup')
def new_student():
   return render_template('signup.html')

@app.route('/welcome')
def welcome():
   return render_template('signup.html')

if __name__ == '__main__':
   app.run(debug = True,port='5001')