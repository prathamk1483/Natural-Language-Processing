# -*- coding: utf-8 -*-
"""3_pos_tagging .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SFDqaO2JN8apZqALVUcxOTydLbsayVGS
"""

import spacy
from collections import Counter

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Sample text for demonstration
text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation.
"""

# Process the text with spaCy
doc = nlp(text)

# Perform POS tagging and count POS tags
pos_tags = Counter()
for token in doc:
    pos_tags[token.pos_] += 1

# Print frequency list of POS tags
print("Frequency of POS tags:")
for tag, count in pos_tags.items():
    print(f"{tag}: {count}")