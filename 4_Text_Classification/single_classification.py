# Train on the top 3000 words

# Return a boolean list of words from an 'article' are in a 'word list'
def find_features(document_list, training_d_list):
    article_words = set(document_list)
    features = {}
    for w in training_d_list:
    	features[w] = (w in article_words)
    # a boolean dict of words from our list that are in an article 
    return features

training_data = "this sentence string format yellow orange purple green" 
training_data_list  = training_data.split()

sentence = "this is a sentence of words in a string format alfalfa"
sentence_list = sentence.split()

feat = find_features(sentence_list, training_data_list)
print feat
