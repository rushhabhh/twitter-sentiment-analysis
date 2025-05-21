### Assign a sentiment label (Positive, Neutral, Negative) to each cleaned tweet using TextBlob

# Importing necessary libraries
import pandas as pd
from textblob import TextBlob
import os

# Load the file
INPUT_PATH = "data/tweets_clean.csv"
OUTPUT_PATH = "data/tweets_sentiment.csv"

# Apply TextBlob to each clean_text
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    # >0->Positive, <0->Negative, ==0->Neutral
    # Polarity score floats between -1 and +1
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, polarity


def run_sentiment_pipeline():
    # Load cleaned tweets
    df = pd.read_csv(INPUT_PATH)

    print(f"Running sentiment analysis on {len(df)} tweets...")
    results = df["clean_text"].apply(analyze_sentiment)
    df["sentiment"] = results.apply(lambda x: x[0])
    df["polarity"] = results.apply(lambda x: x[1])

    # Save output
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Sentiment results saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    run_sentiment_pipeline()