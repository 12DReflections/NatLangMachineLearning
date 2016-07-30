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
print all_words.most_common(15)

print 'kitty'