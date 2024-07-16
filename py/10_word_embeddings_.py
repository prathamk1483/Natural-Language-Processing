# -*- coding: utf-8 -*-
"""10_word_embeddings .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SFDqaO2JN8apZqALVUcxOTydLbsayVGS
"""

import gensim.downloader as api
import gensim
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt')

# Sample text for word embeddings
text = "I love natural language processing. It is fascinating."

# Method 1: Google News Word2Vec
print("Google News Word2Vec:")
try:
    # Load Google News Word2Vec model (large model, download may take some time)
    model_google_news = api.load('word2vec-google-news-300')
    # Tokenize the text
    words = word_tokenize(text)
    # Filter out words not in vocabulary
    words_in_vocab = []
    for word in words:
        if word in model_google_news.vocab:
            words_in_vocab.append(word)
    # Generate word embeddings
    word_embeddings_google_news = []
    for word in words_in_vocab:
        word_embeddings_google_news.append(model_google_news[word])
    print(word_embeddings_google_news)
except Exception as e:
    print("Failed to load Google News Word2Vec model:", e)

# Method 2: Gensim Word2Vec
print("\nGensim Word2Vec:")
# Tokenize the text
words = word_tokenize(text)
# Train Word2Vec model (small example for demonstration)
corpus = [words]
model_gensim = gensim.models.Word2Vec(corpus, vector_size=100, window=5, min_count=1, workers=4)
# Generate word embeddings
word_embeddings_gensim = []
for word in words:
    word_embeddings_gensim.append(model_gensim.wv[word])
print(word_embeddings_gensim)