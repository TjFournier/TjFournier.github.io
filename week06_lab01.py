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
num_mex = 0
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
print ('trump :',num_trump,'russia :',num_rus,'obama :',num_oba,'fake news :',num_fnews,'mexico :',num_mex)
print('% of tweets that contain trump', 100*(num_trump/len(tweets)))