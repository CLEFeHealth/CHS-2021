# Task 2: Consumer Health Search 2021

## Documents Collection
Participants have access to 2 separate crawls of documents: web documents and social media. The crawls have to be downloaded by participants with the scripts detailed below. Alternatively, registered participants can download an indexed version of the document collection.

    .
    ├── webdoc                 # CommonCrawl Crawler
    ├── social-media           # Reddit and Twitter Crawler
    └── README.md

## Web Crawl

- Crawler code (Inside the zip folder you can find the domain list used for crawling.): [webdoc folder](./Webdoc/) or [zip folder on dropbox](https://www.dropbox.com/s/n2ws9qbc6mdspwn/crawler_code.zip?dl=0) 
- extracted_domains (Includes the list of the crawled/extracted domains): [on dropbox](https://www.dropbox.com/s/wg40cl02u61sfs5/extracted_domains.csv?dl=0)
- extracted_urls (~3 million urls from the extracted domains): [on dropbox](https://www.dropbox.com/s/phvim7v2228bdt1/extracted_urls.csv?dl=0) 
- extracted_meta (the detailed csv file with the same extracted urls and all the detailed meta-information): [on dropbox](https://www.dropbox.com/s/1fsfwmmiea23n5z/extracted_meta.csv?dl=0)



## Social Media 

- Crawler code: [social media/code folder](./social-media/code)
- Extracted IDs:  [social media/CLEF_IDs](./social-media/CLEF_IDs)
### Reddit

In Reddit, users upload posts in the form of the so-called submissions, which are sort of “questions” to which other users can reply. Users reply to submissions with one or more comments. 

The documents that are generated for Reddit consist of the submission (plus the connected metadata) and one comment (and connected metadata) combined in one file.

### Twitter 

Tweets are crawled using [Tweepy](https://www.tweepy.org/) and twitter APIs. The description of the tweet data is mentioned on the following [website](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet). 

The documents that are generated for Twitter consist of single tweets and related metadata.




