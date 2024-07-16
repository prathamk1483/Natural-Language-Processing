# -*- coding: utf-8 -*-
"""8_spam_ham .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SFDqaO2JN8apZqALVUcxOTydLbsayVGS
"""

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset containing spam and ham messages
data = pd.read_csv("spam_ham_messages.csv")

# Data Preprocessing
def preprocess_text(text):
    # Remove punctuation, special characters, and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Convert text to lowercase
    text = text.lower()
    # Tokenize the text into words
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

data['cleaned_message'] = data['message'].apply(preprocess_text)

# Feature Extraction
X = data['cleaned_message']  # Input features (cleaned messages)
y = data['label']   # Target variable (spam or ham)

vectorizer = TfidfVectorizer(max_features=5000)  # Convert text data into numerical representations
X = vectorizer.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building
model = LogisticRegression(max_iter=1000)  # Logistic Regression model
model.fit(X_train, y_train)  # Train the model on the training set

# Model Evaluation
y_pred = model.predict(X_test)  # Predict the labels for the testing set
accuracy = accuracy_score(y_test, y_pred)  # Compute the accuracy of the model
print("Accuracy:", accuracy)