import os
from flask import Flask, render_template
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)
pp.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'reader'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'Exp'
mysql = MySQL(app)

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
        curl = mysql.connection.cursor()
        curl.execute("SELECT * FROM user u WHERE u.username=%s and u.psw =%s",(email,password,))
        user = curl.fetchone()
            if len(user) > 1:
                return render_template('dashboard.html')
            else
                return render_template('index.html')

@app.route('/dashboard')
def index():
      	return render_template('dashboard.html')

@app.route('/logout')
def logout():
        return render_template('logout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=False)

