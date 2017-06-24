import os
import time
import markovify
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=120)
def timed_job():
    # authenticate to twitter
    consumer_key = 'mTJoZfOYNCkN9EOOLKeyp98zJ'
    consumer_secret = 'bjMOJ2h5Ux2HCpkydGzqUglmcDYy7vwcYDzb3zsekzPDhFLAZ8'
    access_token = '878683245675786240-CfMpoFiUXwhXeZQZUCkFPnIZIYEUuIQ'
    access_token_secret = 'Aisdl2UyXE0EnnQGZKqFB2TBheptmwWgiUBJcZq7E4dnR'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # markovify
    with open("./whitman.txt") as f:
        text = f.read()
    text_model = markovify.Text(text)

    # tweet
    api.update_status(text_model.make_short_sentence(140))

sched.start()
