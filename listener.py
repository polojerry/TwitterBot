import tweepy
import pprint

pp = pprint.PrettyPrinter(indent=4)


class SimpleListener(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__(api)
        self.me = api.me()
        self.api = api

    def on_status(self, status):
        if status.in_reply_to_status_id is not None or \
                status.user.id == self.me.id:
            print(status.text, " is your own tweet")
            try:
                status.favorite()
            except Exception as e:
                print(e)
            return
        try:
            status.favorite()
            status.retweet()
        except Exception as e:
            print(e)

    # def on_direct_message(self, status):
    #     # code to run each time the stream receives a direct message
    #     pp.pprint(status.text)

    # def on_data(self, status):
    #     # code to run each time you receive some data (direct message, delete, profile update, status,...)
    #     pp.pprint(status)

    def on_error(self, status):
        print(status)


# initialize the stream
# api = create_api()

