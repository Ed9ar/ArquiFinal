from flask import Flask, render_template, request,make_response
from flask_mysqldb import MySQL
import pandas as pd
import streamlit as st
import base64
from io import StringIO
import csv

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'users_twitters'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def UsuarioService():

    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM users")
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    
    return render_template('UsuarioService.html', data=data)

@app.route("/twitter", methods=['GET', 'POST'])
def TwitterService():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        username = request.form.get("username")
        # getting input with name = lname in HTML form 
        twitter = username
        
    print(request.form.get("username"))
    return render_template('TwitterService.html', twitter=twitter)



@app.route("/csv", methods=['GET', 'POST'])
def CSVService():
    cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
    new_column_names = ['City_Name', 'State_Name']
    #cities.to_csv('cities.csv', index=False, header=new_column_names)
    resp = make_response(cities.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    print(cities)
    print(request.form['username'])
    return resp
    #return UsuarioService()


if __name__ == '__main__':
    app.run(debug=True)

