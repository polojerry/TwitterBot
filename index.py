import tweepy
import time
from listener import SimpleListener
import create_api

created_api = create_api.create_api()


def follow_back():
    for follower in tweepy.Cursor(created_api.followers).items(10):
        if not follower.following:
            follower.follow()
            print("You Just followed " + follower.name)
            time.sleep(10)
            follow_back()


if __name__ == "__main__":
    tweepy_listener = SimpleListener(created_api)
    tweepy_stream = tweepy.Stream(auth=created_api.auth, listener=tweepy_listener)

    # put your own keywords here
    tweepy_stream.filter(track=['@dscpwani', "@polojer_ry"]
                         , is_async=True)
    follow_back()
