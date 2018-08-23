# Twitter Sentiment Analysis

Analyzes the sentiment of tweets searched via hashtags .
Takes requests from the page
```
 http://localhost:8000/tweets/<hashtag_keyword>
 example :
 http://localhost:8000/tweets/crowdfunding
 ```
Uses [Sentdex's Sentiment classifier](https://github.com/PythonProgramming/NLTK-3----Natural-Language-Processing-with-Python-series) to analyze Tweets for sentiment


## Getting Started

#### Install depencencies :
```
pip install -r requirement.txt
Fill in Twitter api credentials
```
#### Start Flask App
```
cd twitter-sentiment/
python crawler.py
```

## Built With

* **Python 2.7**
* **Flask 1.0.2**

## Author

* [Sameer Barha](maitto:sameer.barha12@gmail.com)
