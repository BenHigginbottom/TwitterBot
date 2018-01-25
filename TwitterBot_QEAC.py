#!/usr/bin/env python
#Install the tweepy library with 'pip install tweepy' - install pip first!
import tweepy
import os.path

#Obtain these values by creating an app at apps.twitter.com
#Using the account you want to use to tweet
CONSUMER_KEY = "CONSUMER_KEY"
CONSUMER_SECRET = "CONSUMER_SECRET"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"

#Edit these to the user and comment you want to make
#Don't put the @ in the user
#userdispname = "SET ME TO THE USER YOU WANT TO QUOTE"
#comment = "SET ME TO THE COMMENT"

#Search Terms
query = "Queen Elizabeth OR Aircraft Carrier"

#Filters to make sure we get the the right tweets
aircraft = ['no aircraft',
            'without aircraft',
            'aircraftless',
            'planeless',
            'no planes',
            'without planes']

jets = ['no jets',
        'jetless',
        'without jets']

leaking = ['is sinking',
           'is leaking']


#You shouldnt need to make any changes after this point#
#######################################################
#######################################################
#######################################################

#This section sets up the authentication into twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#This looks for an existing tweet id if its been run before
#Might replace with an API call to cut some things down
if os.path.isfile('./lastquoteid.txt'):
    lastquoteid = open('./lastquoteid.txt', 'r').read()
else:
    lastquoteid = "0"

#Creates the link to the tweet
baseurl = "https://twitter.com/" + userdispname + "/status/"

#Gets the last tweet, ignoring retweets and replies 
#lasttweet = api.user_timeline(screen_name = userdispname, count = 1, include_rts = False, exclude_replies = True)

search = api.search(q = query, rpp = 100, since_id = lastid, results_type = recent, include_rts = False, exclude_replies = False)


#And now the logic and the update/post
for stuff in lasttweet:
    lastid = str(stuff.id)
    if lastquoteid == lastid:
        break
    else:
        try:
            quoteurl = baseurl + lastid
            response = " " + comment + " %s " % quoteurl
            s = api.update_status(response)
            f = open('./lastquoteid.txt', 'w')
            f.write(lastid)
            f.close()
        except tweepy.TweepError as e:
            break