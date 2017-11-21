import os
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize,sent_tokenize
from nltk import PorterStemmer
from nltk.corpus import stopwords
import normalization

#Tokenise,remove punctuation and convert to lowercase and removing stopwords.
def tokenize(f):

    processed=[]
    stop_words = set(stopwords.words('english'))
    f = f.lower()

    for word in word_tokenize(f):
        if word.isalnum():
            if word not in stop_words:
                processed.append(word)

    return processed

#Normalization
def normalize(f):
    
    f = normalization.normalize(f)
    f = sent_tokenize(f)
    processed = []

    for u in range(0,len(f)):
        tokens = tokenize(f[u])
        processed.extend(tokens)

    return processed

#Stemming
def stem_words(f):
    
    stemmer=PorterStemmer()
    processed=normalize(f)
    
    for i in range(len(processed)):
        processed[i]=stemmer.stem(processed[i])
    
    return processed

#Preprocess
def textprocess(data):
    
    nltk.data.path.append("/Users/yashsrivastava/Documents/Files/IR/nltk_data")

    processed=stem_words(data)
    return processed

#Text-Extraction
def extract(file):
    
    with open(file, 'r') as myfile:
        data=myfile.read().replace('\n', '')

    soup = BeautifulSoup(data, "html.parser")

    if soup.find('text')!=None:
        return soup.find('text').text        

#Summarization Text
def summarize_text(file,text):

    text[file] = extract(file)

def query_type(query):
    
    if len(query.split())==1:
        return 'OWQ' #One Word Query
    else:
        return 'PQ' #Phrase Query

    '''elif len(query.split()) > 1:
        return 'FTQ' #Free Text Query'''

