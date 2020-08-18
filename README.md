# expense-monitor
A simple expense monitor in python
Flask server, Mysql DB 


git clone https://github.com/3dvolt/expense-monitor.git

create db in Mysql with the .sql file

create user to login in the platform:

INSERT INTO `user` VALUES (1,'Mario','Rossi','user','m.r@gmail.com','exp1234');

pip install mysql-connector-python
pip install flask

python3 START.py

login with the credential:
user - exp1234 


Login Page

![alt text](https://github.com/3dvolt/expense-monitor/blob/master/1.JPG)

After Login, The main page:

![alt text](https://github.com/3dvolt/expense-monitor/blob/master/2.JPG)

Features:
Adding income and expenses
track the fuel consuming, the frequencies of refueling
Setting Expenses in the future
Calendar that shows each expenses and income divided by day
