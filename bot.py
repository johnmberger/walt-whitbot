import os
import time
import markovify
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler

# schedule tweets for every 2 hours
sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=120)
def timed_job():
    # authenticate to twitter
    consumer_key = 'xxxx'
    consumer_secret = 'xxxx'
    access_token = 'xxxx'
    access_token_secret = 'xxxx'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # markovify
    with open("./whitman.txt") as f:
        text = f.read()
    text_model = markovify.Text(text)
    tweet = text_model.make_short_sentence(140)

    # tweet
    print(tweet)
    api.update_status(tweet)

sched.start()
