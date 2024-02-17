# import tweepy
# import sys

# version = sys.version

# api_key = "BMru0QiK0keEvEimmRhIQ6Yz9"
# api_secret = "SGirTFeG4m5aMjjcMqpT8eMex0nz8T4R9NEyDdDx1wVGF9U9EU"
# bearer_token = r"AAAAAAAAAAAAAAAAAAAAADjqpAEAAAAAghVxNJWYOsYN8xVItz4ig7l2JVE%3D9hKaUlaG1rUKrYrEjRQUYgFMbRVaHy4Za7AKYj9MU0BjkdNxLM"
# access_token = "2744777140-tn3RK3teqF17jWEknzPBL7Vh2LmPqSNplflxZhR"
# access_token_secret = "lbBoJkwFL4Tqr2ZA63Ve396cNRQEYfp4PRTj6WGQ4AXSn"

# client = tweepy.Client(
#     bearer_token, api_key, api_secret, access_token, access_token_secret
# )

# auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
# api = tweepy.API(auth)

# client.create_tweet(text="Test")


import tweepy
import random

API_SETUP = {
    "consumer_key": "OO8Jh1A97Zp70B282nHLXS42x",
    "consumer_secret": "9MuXhIXTFYvqHpG8yesHSvUxyREPv8QSU8PjRonjLa4Q7wL7li",
    "bearer_token": r"AAAAAAAAAAAAAAAAAAAAANeupgEAAAAAnHmJ7fCkB8hwbxJ5z0FkzpwXzbA%3Dc1GG65gewp97NlFVCYaOIyi83LsOWdxlvsWEVYx8IqUSE6q7CL",
    "access_token": "1693270022011990024-6y1zGz8CsLAv72Ib3NVp4rCvguuc2b",
    "access_token_secret": "oeUIok99RYfqbzhWlH9QoSvsfGFRDACvB75TZChGC6y9i",
}


class AutoTweet:
    def __init__(self):
        self.client = tweepy.Client(**API_SETUP)

    def send_tweet(self):
        d20 = random.randint(1, 20)
        self.client.create_tweet(text=f"Rolling a d20 every hour... Result: {d20}")


AutoTweet().send_tweet()
