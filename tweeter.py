from twython import Twython
import tweetGenerator
import os

if os.path.isfile("auth.secret"):
    consumer_key, consumer_secret, access_token, access_token_secret = [line.strip('\n') for line in open("auth.secret")]
else:
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']


twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

message = tweetGenerator.generate()

twitter.update_status(status=message)

print("Tweeted: ", message)
