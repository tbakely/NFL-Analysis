import tweepy
import sys

version = sys.version

api_key = "BMru0QiK0keEvEimmRhIQ6Yz9"
api_secret = "SGirTFeG4m5aMjjcMqpT8eMex0nz8T4R9NEyDdDx1wVGF9U9EU"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAADjqpAEAAAAAghVxNJWYOsYN8xVItz4ig7l2JVE%3D9hKaUlaG1rUKrYrEjRQUYgFMbRVaHy4Za7AKYj9MU0BjkdNxLM"
access_token = "2744777140-tn3RK3teqF17jWEknzPBL7Vh2LmPqSNplflxZhR"
access_token_secret = "lbBoJkwFL4Tqr2ZA63Ve396cNRQEYfp4PRTj6WGQ4AXSn"

client = tweepy.Client(
    bearer_token, api_key, api_secret, access_token, access_token_secret
)

# auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
# api = tweepy.API(auth)

# client.create_tweet(text=f"Test. Sent using {version}.")

client.like(1687844588264869888)
