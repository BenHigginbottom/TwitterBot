
!/usr/bin/env python
#Install the tweepy library with 'pip install tweepy' - install pip first!
import tweepy
import os.path

#Obtain these values by creating an app at apps.twitter.com
#Using the account you want to use to tweet
CONSUMER_KEY = "CONSUMER_KEY"
CONSUMER_SECRET = "CONSUMER_SECRET"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"

#Search Terms
query = "Queen Elizabeth OR Aircraft Carrier AND jet OR aircraft OR leak OR sink"

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


########################################################
########################################################
#You shouldnt need to make any changes after this point#
########################################################
########################################################

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

#Search Twitter
search = api.search(q = query, count = 100, since_id = lastquoteid, include_rts = False, exclude_replies = False)

#And now, the logic
idarray = []
for twid in search:
    idarray.append(twid.id)

lastid =  str(idarray[0])
if lastquoteid == lastid:
    print "No New Tweets Found"
else:
    f = open('./lastquoteid.txt', 'w')
    f.write(lastid)
    f.close()
    try:
        for s in search:
            for a in aircraft:
                if a in s.text:
                    screen_name = s.user.screen_name
                    response = "@%s Helicopters are aircraft" % screen_name
                    s = api.update_status(response, s.id)
            for j in jets:
                if j in s.text:
                    screen_name = s.user.screen_name
                    response = "@%s The F35 testing begins later this year" % screen_name
                    s = api.update_status(response, s.id)
            for l in leaking:
                if l in s.text:
                    screen_name = s.user.screen_name
                    response = "@%s This is what sea trials are for, issues will be found and fixed!" % screen_name
                    s = api.update_status(response, s.id)
    except tweepy.TweepError as e:
        print e