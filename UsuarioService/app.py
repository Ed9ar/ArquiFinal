from flask import Flask, render_template, request,make_response
from flask_mysqldb import MySQL
import pandas as pd
import streamlit as st
import base64
import json
from flask import jsonify
from io import StringIO
import csv
import requests

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'comicwire_admin'
app.config['MYSQL_PASSWORD'] = 'AdminPassComicwire1234'
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
  
    u = request.form.get("username")
    u = u.replace('@', '')
    
    stringRequest = requests.get("http://127.0.0.1:8000/?username="+u)
    tweets = json.loads(str(stringRequest.text))
    
    return render_template('TwitterService.html', tweets=tweets, u=u)



@app.route("/csv", methods=['GET', 'POST'])
def CSVService():
    u = request.form.get("username")
    u = u.replace('@', '')
    
    stringRequest = requests.get("http://127.0.0.1:8001/?username="+u)
    print("HOLA")
    print(stringRequest.text)

    return UsuarioService()


if __name__ == '__main__':
    app.run(debug=True)

