from pymongo import *
import tweepy
import json


f = open("mytweets.csv", "w")
f.write("latitude,longitude\n")

client = MongoClient('localhost', 27017)
db = client['']

collection = db['']
tweets = collection.find({})


f.close()