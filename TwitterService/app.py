
from flask import Flask, render_template, request,make_response
import tweepy
from tweepy import OAuthHandler
import json
app = Flask(__name__)

customer_key ='zzoPfSa0AhnSs2vtwpAShVj3P'
customer_secret ='fZ3C0wGgAPcGvnt5N7kO3SOEFEId8Oow2wjUk4tvNRtiefHnuF'
acces_token ='4871223373-HebkdIDGlwAXM2U6AS6vP7ZUjT212kvJPrHBEyO'
access_token_secret ='CRbXHDCCSIfrqyHRiH3VGoTzO5vEV8ATzCGxnL7Y58vvx'
auth = OAuthHandler(customer_key, customer_secret)
auth.set_access_token(acces_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

@app.route('/', methods=['GET', 'POST'])
def tweet():
    username = request.args.get('username')
  
    tweets = api.user_timeline(screen_name=username, 
                           # 200 is the maximum allowed count
                           count=10,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    status = tweets
    json_str = json.dumps(status)

    return str(json_str)

if __name__ == '__main__':
   app.run(host='0.0.0.0')  