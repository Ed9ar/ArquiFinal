from flask import Flask, render_template, request,make_response
import pandas as pd
import streamlit as st
import base64
import json
from flask import jsonify
from io import StringIO
import csv
import requests
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app




app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate("arqui-final-firebase-adminsdk-th57l-b4505957a8.json")
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('users')

@app.route("/", methods=['GET', 'POST'])
def UsuarioService():
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            data =  jsonify(todo), 200
            print("no")
            return render_template('UsuarioService.html', data=data)
        else:
            data = []
            for doc in todo_ref.stream():
                data.append(doc.to_dict()["user"])

            return render_template('UsuarioService.html', data=data)
    except Exception as e:
       return render_template('UsuarioService.html', data=[])
    

@app.route("/twitter", methods=['GET', 'POST'])
def TwitterService():
  
    u = request.form.get("username")
    u = u.replace('@', '')
    
    stringRequest = requests.get("http://10.1.0.33:5000/?username="+u)
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
    app.run(host='0.0.0.0')

