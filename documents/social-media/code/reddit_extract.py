import errno
import json
import os

import numpy as np
import praw
import requests


## This code will crawl the reddit data given the Reddit_ID file.
## Reddit_ID File would be of the format: (ID)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


## Reddit ID files
file = "../CLEF_IDs/reddit_150.csv" #PATH TO REDDIT IDs. 
reddit_ids = np.loadtxt(file, delimiter=",", dtype=object)

## Authentication values for Reddit
client_id = '' #YOUR CLIENT ID
client_secret = '' #YOUR SECRET ID
user_agent = '' #YOUR APP NAME 

for id in reddit_ids:
    try:
        ## Getting Submission using ID
        A = requests.get("http://api.pushshift.io/reddit/search/submission/?ids=%s" % id.split("_")[0]).json()
    except:
        print("Connection not available, sleeping for 2 secs")
        import time

        time.sleep(2)

    ## PRAW authentication for crawling comments
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                         user_agent=user_agent)

    submission = reddit.submission(id=id.split("_")[0])
    missy_comment_lists = []
    from praw.models import MoreComments

    try:
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            missy_comment_lists.append(top_level_comment)
    except:
        import time

        print("Something wrong in comment extraction, sleeping for 2 secs")
        time.sleep(2)
    tmp = []
    comment_id = id.split("_")[-1]
    for missy_comments_list in missy_comment_lists:
        try:
            ## Getting Comment from the specified submission
            if missy_comments_list.id == comment_id:
                tmp_comment = {}
                tmp_comment['id'] = missy_comments_list.id
                tmp_comment['created_utc'] = missy_comments_list.created_utc
                tmp_comment['body'] = missy_comments_list.body.replace("\n", " ")
                tmp_comment['subreddit_name'] = missy_comments_list.subreddit.display_name
                tmp_comment['score'] = missy_comments_list.score
                tmp_comment['ups'] = missy_comments_list.ups
                tmp_comment['parent_id'] = missy_comments_list.parent_id
                tmp_comment['author_name'] = missy_comments_list.author.name
                tmp_comment['author_flair_text'] = missy_comments_list.author_flair_text
                A["data"][0]["comment"] = tmp_comment
        except:
            continue

    ## Creating Folder for saving the crawled data
    folder_path = "%s/Reddit/%s" % ("/".join(file.split("/")[:-1]), id.split("_")[0])
    if not os.path.isdir(folder_path):
        mkdir_p(folder_path)

    ## File Path for document
    file_path = "%s/%s.json" % (folder_path, id)

    with open(file_path, "w") as f:
        json.dump(A, f)
