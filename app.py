from flask import Flask, render_template, request,make_response
from flask_mysqldb import MySQL
import pandas as pd
import streamlit as st
import base64
import tweepy
from tweepy import OAuthHandler

from io import StringIO
import csv

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'users_twitters'

customer_key ='zzoPfSa0AhnSs2vtwpAShVj3P'
customer_secret ='fZ3C0wGgAPcGvnt5N7kO3SOEFEId8Oow2wjUk4tvNRtiefHnuF'
acces_token ='4871223373-HebkdIDGlwAXM2U6AS6vP7ZUjT212kvJPrHBEyO'
access_token_secret ='CRbXHDCCSIfrqyHRiH3VGoTzO5vEV8ATzCGxnL7Y58vvx'
auth = OAuthHandler(customer_key, customer_secret)
auth.set_access_token(acces_token, access_token_secret)
api = tweepy.API(auth)


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
    #print("OIHOIHSIOAHOISHIOAH")
    u = request.form.get("username")
    u = u.replace('@', '')
    
    print(u)
    tweets = api.user_timeline(screen_name=u, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    for info in tweets[:3]:
        print("ID: {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        print("\n")
    #print(tweets)
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

