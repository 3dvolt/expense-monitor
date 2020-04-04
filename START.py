import os
import datetime
from flask import Flask, render_template, request
import mysql.connector

userID = 1
username="User"
currentMonth = datetime.datetime.today().month
months = ["Unknown","January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September","October","November","December"]
app = Flask(__name__)
select = mysql.connector.connect(
  host="localhost",
  user="reader",
  passwd="password",
  database="Exp"
)
insert = mysql.connector.connect(
  host="localhost",
  user="inserter",
  passwd="inSERT",
  database="Exp"
)

@app.route('/')
def index():
      	return render_template('index.html')

@app.route('/fuel')
def fuel():
        mycursor = select.cursor()
        mycursor.execute("SELECT f.data, f.cash FROM fuel f where FK_userId = %s order by ID desc LIMIT 1", (userID,))
        ultimoRif = mycursor.fetchall()
        mycursor.execute("select f.data,f.cash from fuel f where MONTH(f.data) = %s AND FK_userId = %s", (currentMonth ,userID,))
        cashmonth = mycursor.fetchall()
        mycursor.execute("SELECT * FROM fuel where FK_userId = %s ", (userID,))
        query = mycursor.fetchall()
        litriKm =[]
        for x in range(len(query)):
            litri = float(query[x][2]) / float(query[x][1])
            km = 1
            if x != len(query) - 1:
                km = float(query[x + 1][3]) - float(query[x][3])
            litriKm.append( litri / km )
        templateData = {
					'ultimoRif' : ultimoRif[0][0],
                    'costultimoRif': ultimoRif[0][1],
                    'litriKm': litriKm[-2],
                    'euromese' : cashmonth[1],
                    'mese' : months[currentMonth],
					'username' : username
				}
        return render_template('gasoline.html',**templateData)
        
@app.route('/check',methods=["GET","POST"])
def usercheck():
    if request.method == 'POST':
        email = request.form['user']
        password = request.form['psw']
        mycursor = select.cursor()
        mycursor.execute("SELECT * FROM user u WHERE u.username = %s and u.psw = %s",(email,password,))
        myresult = mycursor.fetchall()
        if len(myresult) == 1:
            global userID
            userID = myresult[0][0]
            global username
            username = myresult[0][1]
            return dashboard()
        else:
            return render_template('index.html')

@app.route('/dashboard')
def dashboard():
        print(userID)
        print(username)
        return render_template('dashboard.html')

@app.route('/insert', methods=["GET","POST"])
def incomeOutgo():
    if request.method == 'POST':
        inout = request.form['INorOUT']
        costo = request.form['cost']
        data = request.form['data']
        #linked = request.form['linked']
        category = request.form['Cat']
        mycursor = insert.cursor()
        mycursor.execute("insert into activity values(default, %s, %s, '-', %s, %s, %s)",(inout,costo,data,category,userID,))
        insert.commit()
        return dashboard()

@app.route('/insertgas', methods=["GET","POST"])
def benz():
    if request.method == 'POST':
        costo = request.form['cost']
        costoLitro = request.form['litcost']
        data = request.form['data']
        kmauto = request.form['totKm']
        mycursor = insert.cursor()
        mycursor.execute("Insert into fuel values(default, %s ,%s ,%s ,%s ,%s)",(costoLitro,costo,kmauto,data,userID,))
        insert.commit()
        return dashboard()

@app.route('/logout')
def logout():
        return render_template('logout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=False)

