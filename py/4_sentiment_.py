# -*- coding: utf-8 -*-
"""4_sentiment .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SFDqaO2JN8apZqALVUcxOTydLbsayVGS
"""

from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')

# Sample text for demonstration
text = "I love this movie! It's so uplifting and heartwarming. However, the ending made me sad."

# Sentiment analysis using TextBlob
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
sentiment_label = "positive" if sentiment > 0 else "negative"

print("Sentiment (TextBlob):", sentiment_label)

# Emotion detection using NLTK
sia = SentimentIntensityAnalyzer()
tokens = word_tokenize(text)
emotion_scores = sia.polarity_scores(text)

# Determine emotion based on the sentiment scores
emotion_label = None
if emotion_scores['pos'] > emotion_scores['neg']:
    emotion_label = "positive"
elif emotion_scores['pos'] < emotion_scores['neg']:
    emotion_label = "negative"
else:
    emotion_label = "neutral"

print("Emotion (NLTK):", emotion_label)