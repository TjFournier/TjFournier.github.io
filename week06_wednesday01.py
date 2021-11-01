tweets_str = '''[
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12

    }
]
'''
import json
tweets = []
files = ['/Users/tjfournier19/Downloads/condensed_2009.json','/Users/tjfournier19/Downloads/condensed_2010.json','/Users/tjfournier19/Downloads/condensed_2011.json','/Users/tjfournier19/Downloads/condensed_2012.json','/Users/tjfournier19/Downloads/condensed_2013.json','/Users/tjfournier19/Downloads/condensed_2014.json','/Users/tjfournier19/Downloads/condensed_2015.json','/Users/tjfournier19/Downloads/condensed_2016.json','/Users/tjfournier19/Downloads/condensed_2017.json','/Users/tjfournier19/Downloads/condensed_2018.json',]
for file in files:
    with open(file, encoding='ascii') as f:
        text = f.read()
        tweets += json.loads(text)

num_trump = 0
num_rus = 0
num_oba = 0
num_fnews = 0
num_trump = 0
for tweet in tweets:
    if 'trump' in tweet['text'].lower():
        num_trump += 1
    if 'russia' in tweet['text'].lower():
        num_rus += 1
    if 'obama' in tweet['text'].lower():
        num_oba += 1
    if 'fake news' in tweet['text'].lower():
        num_fnews += 1
    if 'mexico' in tweet['text'].lower():
        num_mex += 1
print ('number_of_tweets=',len(tweets))
print ('num_Trumps=', num_trump)


import pprint #pretty print