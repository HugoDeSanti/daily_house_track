import constants
import tweepy
from track_finder import find_a_track


def post_a_track():
  # Authenticate to Twitter
  client = tweepy.Client(consumer_key=constants.twitter_api_key,
                        consumer_secret=constants.twitter_api_key_secret,
                        access_token=constants.twitter_access_token,
                        access_token_secret=constants.twitter_access_token_secret)

  track_info = find_a_track()
  # track_info is now a dict() with the following keys:

  # track_info["Track"]
  # track_info["Artist"]
  # track_info["BPM"]
  # track_info["Danceability"]
  # track_info["URL"]

  tweet = "Track: " + track_info["Track"]
  tweet += "\n"
  tweet += "Artist: " + track_info["Artist"]
  tweet += "\n"
  tweet += "BPM: " + str(track_info["BPM"])
  tweet += "\n"
  tweet += "Danceability: " + track_info["Danceability"]
  tweet += "\n"
  tweet += track_info["URL"]
  try:
    response = client.create_tweet(text=tweet)
  except:
    print("ERROR")
    print(response)

if __name__ == "__main__":
  post_a_track()

