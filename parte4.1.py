from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from pymongo import MongoClient
import json

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

client = MongoClient('localhost', 27017)
db = client[]
collection = db[]

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    # If the listener recieves data
    def on_data(self, data):
        tweet = json.loads(data)
        if tweet["text"]:
            print (tweet['text'])
            collection.insert(tweet)
        return True

    # If the listener recieves an error
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    # Filtre los tweets!
    stream.filter()
