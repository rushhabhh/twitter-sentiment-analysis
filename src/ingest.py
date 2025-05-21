# Below code is used to downlaod the twitter tweets into the JSON file using Twitter API (TWEEPY), just incase if TWEEPY fails,  
# it will download the tweets using snscrape libaray, where tweet contains keyword: Machine Learning.
# To take the security measures API credentials are not hardcoded, instead they are stored in .env file

# Importing required libraries
import os
import json
from dotenv import load_dotenv

# Twitter API v2
import tweepy
import snscrape.modules.twitter as sntwitter

# Load environment variables from .env
load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
OUTPUT_FILE = "data/tweets_raw.json"

# Fetch the tweets containing a keyword (machine learning) and store as structured JSON
def fetch_tweets_api_v2(query="Machine Learning", count=20):

    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    print("Fetching tweets using Twitter API v2...")
    response = client.search_recent_tweets(
        query=query,
        max_results=min(count, 100),
        tweet_fields=["id", "text", "created_at", "lang"]
    )

    tweets = []
    # extract only key metadata from the 
    if response.data:
        for tweet in response.data:
            tweets.append({
                "id": tweet.id,
                "created_at": tweet.created_at.isoformat(),
                "text": tweet.text
            })

    return tweets


# Will run only incase the TWEEPY API call in failing
def fetch_tweets_scrape(query="Machine Learning", count=20):
    
    print("Falling back to snscrape...")
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= count:
            break
        tweets.append({
            "id": tweet.id,
            "created_at": tweet.date.isoformat(),
            "text": tweet.content
        })
    return tweets

# Save tweets locally into the JSON File
def save_to_file(tweets, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(tweets, f, indent=2)
    print(f"Saved {len(tweets)} tweets to {file_path}")


if __name__ == "__main__":
    try:
        tweets = fetch_tweets_api_v2(query="machine learning", count=20)
        if not tweets:
            raise ValueError("No tweets returned from API.")
    except Exception as e:
        print("API error:", e)
        tweets = fetch_tweets_scrape(query="machine learning", count=20)

    save_to_file(tweets, OUTPUT_FILE)