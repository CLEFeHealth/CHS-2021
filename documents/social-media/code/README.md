# CLEF_SM
CLEF Social Media Crawling code


# Setting up
1. Python 3.x
2. Credentials for Reddit and Twitter API.
3. Install python packages as mentioned below:

```bash
pip install -r requirements
```

# Credentials for Reddit API

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Select “script” as the type of app.
3. Name your app and give it a description.
4. Set-up the redirect uri to be http://localhost:8080.

You will get a box showing your client_id, client_secrets and name, Change the credentials in reddit_extract.py

# Credentials for Twitter

1. Go to https://apps.twitter.com/app/new and log in.
2. Fill in the "Create an application" form.
3. Click on "Create my access token" to generate your token.
4. Copy the following keys from your Twitter app
- Consumer key
- Consumer secret
- Access token
- Access token secret

Change the credentials in twitter_extract.py

# Description of Code

1. Reddit_extract.py : Given the csv file consisting ID. reddit document is crawled and saved in the form of json files along with meta data.
2. Twitter_extract.py : Given the csv file consisting ID. reddit document is crawled and saved in the form of json files along with meta data.

# Example of CSV file

| ID  |
| ------------- |
|  1362922713300561930  |
|  1362922713300561923  |
