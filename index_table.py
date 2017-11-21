from nltk import word_tokenize
from nltk import PorterStemmer
from nltk.corpus import stopwords
import nltk
import collections

import os
import json
import time

nltk.data.path.append("/Users/yashsrivastava/Documents/Files/IR/nltk_data")

#tokenise,remove punctuation and convert to lowercase

def tokenize(f):
	processed=[]
	for line in f.readlines():
		for word in word_tokenize(line):
			if word.isalnum():
				processed.append(word.lower())
	return processed

#stemming

def stem_words(f):
	stemmer=PorterStemmer()
	processed=tokenize(f)
	for i in range(len(processed)):
		processed[i]=stemmer.stem(processed[i])
	return processed

#remove stopwords

def remove_stopwords(f):
	processed=stem_words(f)
	for word in processed:
		if word in stopwords.words('english'):
			processed.remove(word)
	return processed

#preprocess

def preprocess(f):
	processed=remove_stopwords(f)
	return processed

#traverse through files

def create_index_table(filepath):

	start=time.time()
	index_table=[]

	for folder,subfolders,files in os.walk(filepath):

		for filename in files:

			processed=preprocess(open(os.path.join(os.path.abspath(folder),filename)))

			for word in processed:

				term=word
				document=os.path.join(os.path.abspath(folder),filename)
				index_table.append((term,document))

	index_table=sorted(index_table)

	index_table_final= collections.defaultdict()
	prev_word=''

	for i in range(len(index_table)):

		term=index_table[i][0]
		document=index_table[i][1]

		if prev_word==term:
			index_table_final[term][0].append(document)

		else:
			index_table_final[term] = {}
			index_table_final[term][0]=[document]

		prev_word=term

	for term in index_table_final:
			index_table_final[term][1] = len(index_table_final[term][0])


	end=time.time()
	print end-start
	return index_table_final

if __name__=="__main__":
	ind_table=create_index_table("data/text_data")
	f=open("data/index_table.json",'w')
	json.dump(ind_table,f)
