import tweepy
import csv
import pandas as pd
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
tok = WordPunctTokenizer()
import sentiment_mod as s
import hashlib

import sys
reload(sys)
sys.setdefaultencoding('utf8')

##
consumer_key = 'OWdAlaMxTUs1SSUmZqfRIg9ZL'
consumer_secret = 'yZhnFUNkIznFRB1YljceO0TcChDvYH3k9jd0ptPacXDhG75aNA'
access_token = '320616006-KlvozMK2O88mxE6zWEQxOy2j7e2Pw2vcwUFEOLFa'
access_token_secret = 'M8FMqzAo7iSpA6QErIGXd79y8W8udQTVXGRChYEHit63i'

#Cleaning Params
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))

def tweet_cleaner(text):
    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    '''
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    '''
    lower_case = souped.lower()
    # During the letters_only process two lines above, it has created unnecessay white spaces,
    # I will tokenize and join together to remove unneccessary white spaces
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()

def get_tweets():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    #####United Airlines
    # Open/Create a file to append data
    csvFile = open('ua.csv', 'a')
    csvClean = open('clean.csv','a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
    csvWClean = csv.writer(csvClean)

    cnt =0
    ctweets = list()
    csets = set()
    sent = list()
    for tweet in tweepy.Cursor(api.search,q="#ico",count=100,
                               lang="en", since="2017-04-03").items():
        #print (tweet.created_at, tweet.text)
        #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        #csvWriter.writerow([tweet.text.encode('utf-8')])
        clean_tweet = tweet_cleaner(tweet.text.encode('utf-8'))

        h = hashlib.md5()
        h.update(clean_tweet.encode('utf-8'))
        hash_val = h.hexdigest()

        if hash_val not in csets:
            ctweets.append(clean_tweet.encode('utf-8'))
            csets.add(hash_val)

            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
            csvWClean.writerow([clean_tweet.encode('utf-8')])

            print (tweet.created_at, clean_tweet)
            sentiment_value, confidence = s.sentiment(clean_tweet.encode('utf-8'))

            sent.append(sentiment_value)
            cnt+=1

        if cnt==20:
            break

        #print '{}'.format(clean_tweet.encode('utf-8'))
        #csvWClean.writerow([clean_tweet.encode('utf-8')])
        #sentiment_value, confidence = s.sentiment(clean_tweet.encode('utf-8'))
        #print '===> {} ---> {} '.format(sentiment_value, confidence )
    print ctweets
    print sent

    #return ctweets, sent


get_tweets()
