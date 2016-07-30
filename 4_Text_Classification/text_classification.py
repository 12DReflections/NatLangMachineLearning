import nltk
import random
from nltk.corpus import movie_reviews

# Text Classification with nltk library
# Works if you have a body of a words and a boolean classification ie (positive, negative) as a tuple


documents = [(list(movie_reviews.words(fileid)), category) 
				for category in movie_reviews.categories() 
				for fileid in movie_reviews.fileids(category)]

# # Same as 
# documents = []
# for category in movie_reviews.categories():
# 	for fileid in movie_reviews.fileids(category):
# 		documents.append(list(movie_reviews.words(fileid)), category)

# Train data
random.shuffle(documents)

# Get the full list of words
all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

# Convert list to frequency distribution and print most common words
all_words = nltk.FreqDist(all_words)
#print all_words.most_common(15)

# Train on the top 3000 words
word_features = list(all_words.keys())[:3000]
# training_data = "this sentence string format yellow orange purple green" 
# word_features  = training_data.split()

# A set removes doubled elements, only single representation
def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		# (w in words) creates boolean value for each word, if word in document it will return true, else it will return false
		features[w] = (w in words) 
	return features

# sentence = "this is a sentence of words in a string format alfalfa"
# feat = find_features(sentence)
# print feat

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]


print 'kitty'