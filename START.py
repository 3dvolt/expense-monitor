import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
      	return render_template('index.html')

@app.route('/fuel')
def fuel():
        return render_template('gasoline.html')
        
@app.route('/check')
def user():
        return render_template('dashboard.html')

@app.route('/dashboard')
def index():
      	return render_template('dashboard.html')

@app.route('/logout')
def logout():
        return render_template('logout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=False)

