import errno
import json
import os

import numpy as np
import tweepy


## This code will crawl the reddit data given the Tweet_ID file.
## Tweet_ID File would be of the format: (ID)
## PLEASE provide the absolute path for the ID file





## Function for extraction of the Status using tweepy
def lookup_tweets(tweet_IDs, api):
    full_tweets = []
    tweet_count = len(tweet_IDs)
    try:

        for i in range(tweet_count):
            full_tweets.append(
                api.get_status(tweet_IDs[i])
            )
        return full_tweets
    except tweepy.TweepError:
        print('Something went wrong, quitting...')


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

## Authentication of Twitter (Change it according to your own credentials)


consumer_key = "" #YOUR CONSUMER KEY
consumer_secret = "" #YOUR CONSUMER SECRET
access_token =  "" #YOUR ACCESS TOKEN
access_token_secret =  "" #YOUR ACCESS TOKEN SECRET
                                                               


## Authentication Object of Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

## Tweet ID File
file="../CLEF_IDs/tweets_150.csv" #PATH TO TWEETS IDs. 
tweets_ids=np.loadtxt(file,delimiter=",",dtype=object)

for tweets_id in tweets_ids:
    results = lookup_tweets([tweets_id], api)

    ## Data Saving Folder
    folder_path = "%s/Twitter/" % ("/".join(file.split("/")[:-1]))
    if not os.path.isdir(folder_path):
        mkdir_p(folder_path)

    ## File Path for saving json file
    file_path="%s/%s.json"%(folder_path,tweets_id)

    if results is not None:
        with open(file_path, "w") as f:
            json.dump(results[0]._json, f)
    else:
        print("Error in extraction....")