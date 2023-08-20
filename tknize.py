import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Read the contents of the file
with open('transcript.txt', 'r') as f1:
    text = f1.read()
 
word_tokens = word_tokenize(text)

print(word_tokens)