import os
import time
import markovify
import tweepy
import random
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

    # randomly generate a 4-line poem or a 140-character string
    boolean = random.choice([True, False])
    
    if boolean == True:
        tweet = ''
        for x in range(0, 4):
            line = text_model.make_short_sentence(30)
            while line == None:
                line = text_model.make_short_sentence(30)
            if x < 3:
                line = line[:-1]
            if x == 0:
                tweet += line
            else:
                tweet += '\n' + line

        print(tweet)
        api.update_status(tweet)
    else:
        tweet = text_model.make_short_sentence(140)
        print(tweet)
        api.update_status(tweet)

sched.start()
