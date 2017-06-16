# coding=utf-8
import tweepy
import matplotlib.pyplot as plt


# Authentication Process
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#for tweet in tweepy.Cursor().items():


# GRAFICO DE BARRAS
dictionary = plt.figure()
#Diccionario con mis datos
D = {}
plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys())
plt.show()



