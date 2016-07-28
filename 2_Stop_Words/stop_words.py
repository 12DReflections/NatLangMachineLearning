from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#import nltk
#nltk.download()

example_sentence = "This sentence is to show how stop word filtration works in the NLTK Library"

# Stop word list, just as easy to create your own list of words to filter out of sentence
stop_words = set(stopwords.words("english"))
#print stop_words

words = word_tokenize(example_sentence)

# If word isn't in stop words, put it in filtered words
#    the converse is to match to a word list as compared to filter
# filtered_sentence = []
# for w in words:
# 	if w not in stop_words:
# 		filtered_sentence.append(w)

#List comprehension equivelant
filtered_sentence = [w for w in words if not w in stop_words]

print filtered_sentence