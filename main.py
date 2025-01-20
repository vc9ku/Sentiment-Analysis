from textblob import TextBlob
import tweepy

# Replace with your own credentials
bearer_token = ''

client = tweepy.Client(bearer_token=bearer_token)

query = 'Trump -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

for tweet in tweets.data:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)