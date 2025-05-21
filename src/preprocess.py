### Below code clean the raw tweet text to remove unnecessary noise like (links, hashtags, tagging(mentions)) and save it for analysis

# Importing required libraries
import json
import pandas as pd
import os
import re # Regex library used for cleaning

# Loading the data
INPUT_PATH = "data/tweets_raw.json"
OUTPUT_PATH = "data/tweets_clean.csv"

# Applying cleaning technique using regex library
def clean_text(text):
    text = re.sub(r"http\S+", "", text) # remove URLs
    text = re.sub(r"@\w+", "", text) # remove tags (mentions)
    text = re.sub(r"#\w+", "", text) # remove hashtags
    text = re.sub(r"RT\s+", "", text) # remove retweet markers
    text = re.sub(r"[^\w\s]", "", text) # remove punctuation
    text = re.sub(r"\s+", " ", text) # remove extra whitespace
    return text.strip()

def preprocess_tweets():
    # Load JSON data
    with open(INPUT_PATH, "r") as f:
        tweets = json.load(f)

    print(f"Loaded {len(tweets)} tweets")

    # Build DataFrame
    df = pd.DataFrame(tweets)
    df["clean_text"] = df["text"].apply(clean_text)

    # Save to CSV
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df[["id", "created_at", "clean_text"]].to_csv(OUTPUT_PATH, index=False)
    print(f"Cleaned tweets saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    preprocess_tweets()