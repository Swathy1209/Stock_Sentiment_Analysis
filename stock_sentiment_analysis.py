import tweepy
from textblob import TextBlob
import pandas as pd

# Twitter API credentials
API_KEY = 'YvgwouG8ew0NSnUNJSEGy5zW5'
API_SECRET = 'tqHP5PPDIBMh7QQTDUOnlpYROJ1WDdv8imceUm16CuZfwc8AOf'
ACCESS_TOKEN = '1845492063678455808-jWThJ7q0xVymAG0IsDYB19P4VoDvF4'
ACCESS_SECRET = '0LI418fkcwdNdnWw4L0j7ejMRautTyVt13KVeThlag6zI'

# Set up authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Function to fetch tweets from a user's timeline
def fetch_tweets(elonmusk ):
    try:
        tweets = api.user_timeline(screen_name=elonmusk, count=100, tweet_mode='extended')
        return tweets
    except tweepy.errors.Forbidden as e:
        print(f"Error: {e}")
        return []

# Function to analyze sentiment of tweets
def analyze_sentiment(tweets):
    data = []
    for tweet in tweets:
        tweet_text = tweet.full_text
        tweet_date = tweet.created_at
        analysis = TextBlob(tweet_text)
        sentiment = analysis.sentiment.polarity  # Polarity ranges from -1 (negative) to +1 (positive)
        data.append([tweet_date, tweet_text, sentiment])
    return data

# Function to save results to a DataFrame and CSV
def save_to_csv(data, filename='tweets_sentiment_analysis.csv'):
    df = pd.DataFrame(data, columns=['Date', 'Tweet', 'Sentiment'])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main function
def main():
    user_screen_name = 'elonmusk'  # Replace with the user's screen name you want to analyze
    tweets = fetch_tweets(user_screen_name)
    
    if tweets:
        sentiment_data = analyze_sentiment(tweets)
        save_to_csv(sentiment_data)

if __name__ == '__main__':
    main()

