from twython import Twython
import tweetGenerator

consumer_key, consumer_secret, access_token, access_token_secret = [line.strip('\n') for line in open("auth.secret")]

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

message = tweetGenerator.generate()

twitter.update_status(status=message)

print("Tweeted: ", message)
