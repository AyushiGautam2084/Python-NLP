import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

st = PorterStemmer()

with open('transcript.txt', 'r') as f1:
    text = f1.read()
 
word_tokens = word_tokenize(text)

stemmed_tokens = [st.stem(token) for token in word_tokens]

# Print the stemmed tokens
print(stemmed_tokens)
