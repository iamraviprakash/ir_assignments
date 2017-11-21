import os
import json
import time

from nltk import PorterStemmer

f=open('data/index_table.json','r')
index_table=json.load(f)

search_term=raw_input("Enter search term:")
search_words=search_term.split()

stemmer=PorterStemmer()

first_word=stemmer.stem(search_words[0])
doc_list=index_table[first_word]

for word in search_words:
	word=stemmer.stem(word)
	doc_list2=index_table[word]
	doc_list=list(set(doc_list) & set(doc_list2))

print doc_list
