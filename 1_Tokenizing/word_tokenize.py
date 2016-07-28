#from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
#nltk.download() #on first use of nltk you need to download the libraries

example_text = 'Ontology is the philosophical study of the nature of being, becoming, existence or reality as well as the basic categories of being and their relations. Traditionally listed as a part of the major branch of philosophy known as metaphysics, ontology often deals with questions concerning what entities exist or may be said to exist and how such entities may be grouped, related within a hierarchy, and subdivided according to similarities and differences. Although ontology as a philosophical enterprise is highly theoretical, it also has practical application in information science and technology, such as ontology engineering'

print nltk.sent_tokenize(example_text)
print nltk.word_tokenize(example_text)