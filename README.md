# Twitter Sentiment Analysis - ML Pipeline
This project demonstrates a complete, modular machine learning pipeline to perform sentiment analysis on recent tweets using a keyword or hashtag. It is designed to be cloud-ready, secure, and easy to extend or automate.

## Project Overview
**Objective:**
Classify the sentiment of tweets (positive, neutral, negative) using a simple and explainable ML model.

**Pipeline Components:**

1. **Ingestion** - Pull tweets using Twitter API or fallback to snscrape
2. **Preprocessing** - Clean and normalize tweet text
3. **Sentiment Analysis** - Run inference using TextBlob
4. **Delivery** - Save results as CSV and visualize with Streamlit

## Folder Structure
twitter-sentiment-/
|- data/                  # Stores raw and processed tweet data
|   |- tweets_raw.json
|   |- tweets_clean.csv
|   |- tweets_sentiment.csv
|- src/                  # Core Python scripts
|   |- ingest.py
|   |- preprocess.py
|   |- sentiment.py
|- dashboard.py          # Streamlit dashboard
|- .env                  # Environment variables (excluded from Git)
|- requirements.txt      # Dependencies
|- README.md             # This file

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/twitter-sentiment-ml.git

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Up Environment Variables
Create a '.env' file:
TWITTER_BEARER_TOKEN=your_bearer_token_here

## Step-by-Step Pipeline Execution

### Ingest Tweets
python src/ingest.py
* Collects tweets via Twitter API (v2)
* Falls back to 'snscrape' if API fails
* Saves 'tweets_raw.json'

### Preprocess Tweets
python src/preprocess.py
* Cleans text: removes URLs, mentions, hashtags, etc.
* Saves 'tweets_clean.csv'

### Run Sentiment Analysis
python src/sentiment.py
* Uses TextBlob to compute polarity and sentiment
* Saves 'tweets_sentiment.csv'

### Launch Dashboard
streamlit run dashboard.py
* Interactively explore sentiment results

## Cloud & ML Design Considerations

### Data Security
* API keys stored in '.env' file (never hardcoded)
* Only public tweet metadata used
* Easily extendable to S3 + IAM roles for cloud storage

### ML Component
* Sentiment model via 'TextBlob' (rule-based)

## Future Improvements
* Swap in fine-tuned transformer model (e.g. BERT)
* Store results in AWS S3 or a cloud database
* Build CI/CD pipeline for automated deploy + retrain