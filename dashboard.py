import pandas as pd
import streamlit as st

# Load results
df = pd.read_csv("data/tweets_sentiment.csv")

st.title("Twitter Sentiment Analysis Dashboard")

# Overall stats
st.subheader("Sentiment Distribution")
sentiment_counts = df["sentiment"].value_counts()
st.bar_chart(sentiment_counts)

# Tweet viewer
st.subheader("Explore Tweets by Sentiment")
selected_sentiment = st.selectbox("Choose sentiment:", df["sentiment"].unique())
filtered = df[df["sentiment"] == selected_sentiment]

st.write(f"Showing {len(filtered)} tweets classified as **{selected_sentiment}**")

st.dataframe(filtered[["clean_text", "polarity"]].reset_index(drop=True))