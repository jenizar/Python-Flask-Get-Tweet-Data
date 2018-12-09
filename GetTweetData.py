#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:14:24 2018

@author: john
"""

from flask import Flask, render_template
from flask import request
from jinja2 import Template
import tweepy
import json
import datetime
from datetime import datetime

t_consumerkey = 'MWQadaodeKZ02FPTfkJB7OhF9'
t_secretkey = 'hVGVTiEtAEFwzLZLB6gpa8IbI2xrdv7l4G9S61QyvI3lrPwcU3'
access_tokenkey = '2942702198-rybhZK6kteq3c1KyIoAAMtV3C49Y8LlU2VkQcz5'
access_tokensecret = 'ErFaebAlbAfL1e4yh2NjEx1VDFdQq8En6OusUbHYyUKKY'

app = Flask(__name__, template_folder="mytemplate")

@app.route('/',  methods=['GET','POST'])
def Search():    
    all_tweets_text = []    
    
    if request.method == 'GET':
        return render_template('TweetPage.html')
    else:            
        name = request.form['name']
        sdate = datetime.strptime(request.form['sdate'], '%Y-%m-%d')
        edate = datetime.strptime(request.form['edate'], '%Y-%m-%d')
      
        auth = tweepy.OAuthHandler(t_consumerkey, t_secretkey)
        auth.set_access_token(access_tokenkey, access_tokensecret)

        api = tweepy.API(auth)

        public_tweets = api.user_timeline(screen_name=name, tweet_mode='extended')
            
        for tweet_info in public_tweets:
            if tweet_info.created_at < edate and tweet_info.created_at > sdate:
               all_tweets_text.append(tweet_info.full_text)  
            
        return render_template('TweetPage.html', _anchor="Search", result=all_tweets_text)

if(__name__) == '__main__':
    app.run(debug=True)  