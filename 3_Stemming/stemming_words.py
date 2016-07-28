from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

word_list = ["quick", "quickly", "quicker"]

for word in word_list:
	print ps.stem(word)

