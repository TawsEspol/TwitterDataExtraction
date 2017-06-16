# coding=utf-8
import tweepy
import json

# Authentication Process
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

## Relice un tweet
api.

## Dele RT al tweet que acaba de crear.
api.

## Elimine el tweet que acaba de crear.
api.
