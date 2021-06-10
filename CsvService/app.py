from flask import Flask, render_template, request,make_response
import json
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def csv():
    user = request.args.get('username')
    print("Esto es User" , user)
    stringRequest = requests.get("http://10.1.0.33:5000/?username="+user)
    tweets = json.loads(str(stringRequest.text))
    return str(stringRequest.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0') 