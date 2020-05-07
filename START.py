import datetime
from flask import Flask, render_template, request, session
import mysql.connector

userID = 1
username="User"
currentMonth = datetime.datetime.today().month
months = ["Unknown","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
app = Flask(__name__)

app.secret_key = '12345678'

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
    if 'loggedin' in session:
        mycursor = select.cursor()
        mycursor.execute("SELECT f.data, f.cash FROM fuel f where FK_userId = %s order by ID desc LIMIT 1", (userID,))
        ultimoRif = mycursor.fetchall()
        mycursor.execute("select f.data,f.cash from fuel f where MONTH(f.data) = %s AND FK_userId = %s", (3 ,userID,))
        cashmonth = mycursor.fetchall()
        mycursor.execute("SELECT * FROM fuel where FK_userId = %s ", (userID,))
        query = mycursor.fetchall()
        litriKm =[]
        print(query)
        for x in range(len(query)):
            litri = float(query[x][2]) / float(query[x][1])
            if x != len(query):
                km = float(query[x + 1][3]) - float(query[x][3])    
            consumo = litri/km
            litriKm.append(round(consumo,2))
        templateData = {'ultimoRif' : ultimoRif[0][0],
                    'costultimoRif': ultimoRif[0][1],
                    'litriKm': litriKm[-1],
                    'euromese' : cashmonth[0][1],
                    'mese' : months[currentMonth],
					'username' : username,
                    'kmtot': km}
        return render_template('gasoline.html',**templateData)
    else:
        index()
        
@app.route('/check',methods=["GET","POST"])
def usercheck():
    if request.method == 'POST':
        email = request.form['user']
        password = request.form['psw']
        mycursor = select.cursor()
        mycursor.execute("SELECT * FROM user u WHERE u.username = %s and u.psw = %s",(email,password,))
        myresult = mycursor.fetchall()
        if len(myresult) == 1:
            session['loggedin'] = True
            session['id'] = myresult[0][0]
            session['username'] = myresult[0][1]
            global userID
            userID = myresult[0][0]
            global username
            username = myresult[0][1]
            return dashboard()
        else:
            return index()

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        mycursor = select.cursor()
        mycursor.execute("select a.data,a.cost,a.causale from activity a where FK_userId= %s AND INorOUT='IN'", (userID,))
        IN = mycursor.fetchall()
        mycursor.execute("select f.data,f.cash from fuel f where FK_userId= %s",(userID,))
        Fuel = mycursor.fetchall()
        mycursor.execute("select a.data,a.cost,a.causale from activity a where FK_userId= %s AND INorOUT='OUT'", (userID,))
        OUT = mycursor.fetchall()
        d = ''
        for x in Fuel:
            datee = ' new Date(' + str(x[0]).replace('-', ',') + ')'
            d += "{'Date':" + datee + ", 'Title': '-" + x[1] + " Benzina' , 'Color': 'blue'},"
        for x in OUT:
            datee = ' new Date(' + str(x[0]).replace('-', ',') + ')'
            d += "{'Date':" + datee + ", 'Title': '-" + x[1] + ' ' + x[2] + " ' , 'Color': 'red'},"
        for x in IN:
            datee = ' new Date(' + str(x[0]).replace('-', ',') + ')'
            d += "{'Date':" + datee + ", 'Title': '+" + x[1] + ' ' + x[2] + "', 'Color': 'green'},"
        templateData = {'username' : session['username'],'calend': d}
        return render_template('dashboard.html',**templateData)
    else:
        return index()

@app.route('/insert', methods=["GET","POST"])
def incomeOutgo():
    if request.method == 'POST':
        inout = request.form['INorOUT']
        costo = request.form['cost']
        data = request.form['data']
        linked = request.form['linked']
        category = request.form['Cat']
        mycursor = insert.cursor()
        mycursor.execute("insert into activity values(default, %s, %s, %s, %s, %s, %s)",(inout,costo,linked,data,category,userID,))
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

@app.route('/settings')
def profile():
    if 'loggedin' in session:
        mycursor = select.cursor()
        mycursor.execute('SELECT * FROM user WHERE ID = %s', (session['id'],))
        account = mycursor.fetchone()
        templateData = {'username': session['username']}
        return render_template('profile.html', **templateData, account=account)
    return index()

@app.route('/tables')
def tables():
    if 'loggedin' in session:
        mycursor = select.cursor()
        mycursor.execute('SELECT InorOut,causale,data,categoria,cost FROM activity WHERE fk_UserId = %s', (session['id'],))
        mov = mycursor.fetchall()
        return render_template('tables.html', mov=mov)
    return index()

@app.route('/logout')
def logout():
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        return render_template('logout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=False)


