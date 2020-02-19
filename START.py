import os
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
  host="localhost",
  user="reader",
  passwd="password",
  database="Exp"
)

@app.route('/')
def index():
      	return render_template('index.html')

@app.route('/fuel')
def fuel():
        return render_template('gasoline.html')
        
@app.route('/check',methods=["GET","POST"])
def logout():
    if request.method == 'POST':
        email = request.form['user']
        password = request.form['psw']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user u WHERE u.username=%s and u.psw =%s",(email,password,))
        myresult = mycursor.fetchall()
        if len(myresult) > 1:
            return render_template('dashboard.html')
        else:
            return render_template('index.html')

@app.route('/dashboard')
def index():
      	return render_template('dashboard.html')

@app.route('/logout')
def logout():
        return render_template('logout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=False)

