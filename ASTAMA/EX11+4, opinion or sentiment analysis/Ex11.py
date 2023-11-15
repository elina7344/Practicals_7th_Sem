import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Download VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')
# Create a SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()
# Sample texts for opinion mining
texts = [
"I love this product! It's amazing.",
"The service was terrible. I'm very disappointed.",
"This movie is neither good nor bad.",
"I don't have any strong feelings about this issue."
]
# Perform sentiment analysis on each text
for text in texts:
    # Analyze the sentiment of the text
    sentiment_scores = sid.polarity_scores(text)
    # Determine the sentiment label based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
        # Print the text and its sentiment
    print(f"Text: '{text}'")
    print(f"Sentiment: {sentiment} (Compound Score: {sentiment_scores['compound']})")
    print("-" * 30)

#OUTPUT
'''
Text: 'I love this product! It's amazing.'
Sentiment: Positive (Compound Score: 0.8516)
------------------------------
Text: 'The service was terrible. I'm very disappointed.'
Sentiment: Negative (Compound Score: -0.7574)
------------------------------
Text: 'This movie is neither good nor bad.'
Sentiment: Negative (Compound Score: -0.5824)
------------------------------
Text: 'I don't have any strong feelings about this issue.'
Sentiment: Negative (Compound Score: -0.4023)
------------------------------
'''
