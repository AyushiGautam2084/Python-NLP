import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
 
lem = WordNetLemmatizer()

with open('transcript.txt', 'r') as f1:
    text = f1.read()
 
word_tokens = word_tokenize(text)

lemmatized_tokens = [lem.lemmatize(token) for token in word_tokens]

print(lemmatized_tokens)
