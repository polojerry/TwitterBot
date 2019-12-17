import tweepy
import auth_keys as auth_keys


def create_api():
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(auth_keys.consumer_key, auth_keys.consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(auth_keys.access_key, auth_keys.access_secret)

    # Calling api
    tweeter_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return tweeter_api
