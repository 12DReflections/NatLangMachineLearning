import nltk
import random
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize

# A naive bayes algorithm, finding the words which lead to a positive/negative classification of an article

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
	words = word_tokenize(document)
	print words
	#print words
	features = {}
	for w in word_features:
		# (w in words) creates boolean value for each word, if word in document it will return true, else it will return false
		features[w] = (w in words) 
	print features
	return features

# sentence = "this is a sentence of words in a string format alfalfa"
# feat = find_features(sentence)
# print feat

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))


clas_sentence = 'refreshingly dismissed madsen'
clas = find_features(clas_sentence)

# The existence of words in a document, from our training words, and whether they lead to a positive/negative category
featuresets = [(find_features(rev), category) for (rev, category) in documents]
#print featuresets[1]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# Naive bayes
# post_occurence = prior_occurrence * liklihood / evidence 
# Show whether a word is more likely to be in a positive or negative review
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Algo accuracy percent: ", (nltk.classify.accuracy(classifier, testing_set)) * 100)
classifier.show_most_informative_features(15)
print classifier.classify(clas)
#print clas

print 'kitty'