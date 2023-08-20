import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Read the contents of the file
with open('transcript.txt', 'r') as f1:
    text = f1.read()
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(text)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
 
print(word_tokens)
print("\n\nAfter removing the stop words:\n\n")
print(filtered_sentence)

