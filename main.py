import os
import numpy as np
import time
from flask import Flask, session, redirect, url_for, escape, request, render_template, Response, flash, abort
from flask_mysqldb import MySQL,MySQLdb
import threading

app = Flask(__name__)

mysql = MySQL(app)

@app.route('/')
def index2():
      	return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        curl = mysql.connection.cursor()
        curl.execute("SELECT * FROM USER u WHERE u.username=%s and u.psw =%s",(name,password,))
        user = curl.fetchone()
        if len(user) > 1:
                return render_template("index.html")
        else:
            	return index()#render_template("login.html")
    else:
        return index()#render_template("login.html")


@app.route('/table')
def table():
      	return render_template('table.html') #table in/out


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
