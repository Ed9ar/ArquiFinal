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

@app.route('/', methods=['GET', 'POST'])
def csv():
    user = request.args.get('username')
    stringRequest = requests.get("http://127.0.0.1:8000/?username="+user)
    tweets = json.loads(str(stringRequest.text))
    t = []
    for tweet in tweets:
        t.append([tweet["id"], tweet["created_at"], tweet["full_text"]])

    
    #print(t)

    tweetsCsv = pd.DataFrame(t, columns=['Id', 'CreatedAt', 'Tweet'])
    new_column_names = ['Id_Name', 'CreatedAt_Name', 'Tweet_Name']
    resp = make_response(tweetsCsv.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=tweets.csv"
    resp.headers["Content-Type"] = "text/csv"
    print(tweetsCsv)
    return resp

if __name__ == '__main__':
    app.run(host="localhost", port=8001, debug=True)   