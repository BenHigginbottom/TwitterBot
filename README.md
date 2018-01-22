# TwitterBot

I've been playing around with the Twitter API the past week when this tweet caught my eye

https://twitter.com/HashtagGriswold/status/955217190688567297

From a reporter in the US, and it appealed to my warped sense of humour - so decided to write one.

## Pre-requisites

Tested with Python 2.7, so this could be run on a Raspberry Pi 

Only external dependency is Tweepy, which assuming pip is installed, can be installed with the following command (Linux)

```bash
pip install tweepy --user
```

All testing has been conducted on Ubuntu Linux, although there isnt anything that would prevent it running on OSX or even Windows

## Setup

There are multiple tutorials on how to setup an app in twitter, so I'll just link to one -

https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

The application will need to be able to read and write to Twitter

## Configuration

With the Consumer and Access keys, the following section of the TwitterBot.py file will need to be updated

```python
CONSUMER_KEY = "CONSUMER_KEY"
CONSUMER_SECRET = "CONSUMER_SECRET"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"
```

And then the user you want to quote without the '@' along with the comment you want to make before the quote here 

```python
userdispname = "SET ME TO THE USER YOU WANT TO QUOTE"
comment = "SET ME TO THE COMMENT"
```

So in Mr Griswold's case these would be

```python
userdispname = "neiltyson"
comment = "*Giant Bong Hit*"
```

Which being the innocent I am, I'm certain is some kind of percussion instrument, like a gong...

## Running

```bash
python ./TwitterBot.py
```

The program maintains a state in a textfile in the same directory as the program. This file contains the last ID of the tweet quoted and will only update the status if there is a new tweet.

There isnt a timer or other daemon yet, so the program will either need to be manually run or setup with a crontab

## To-do

* Convert into a lambda function
* Add in datetime and stick in a sleep function?