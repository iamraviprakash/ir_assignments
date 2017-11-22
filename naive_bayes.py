import os,json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from non_ascii_remover import remove_non_ascii
import nltk
nltk.data.path.append("/Users/yashsrivastava/Documents/Files/IR/nltk_data")

spam=[]
ham=[]

remove_non_ascii('data/sample')

for folder,subfolders,files in os.walk('data/sample/train/spam'):

    for filename in files:

        f=open((os.path.join(os.path.abspath(folder),filename)))
        for word in word_tokenize(f.read().lower()):
            if word.isalnum() and word not in stopwords.words('english') and word!='subject':
                spam.append(word)

        f.close()

for folder,subfolders,files in os.walk('data/sample/train/ham'):

    for filename in files:

        f=open((os.path.join(os.path.abspath(folder),filename)))
        for word in word_tokenize(f.read().lower()):
            if word.isalnum() and word not in stopwords.words('english') and word!='subject':
                ham.append(word)

        f.close()

V=len(list(set(spam+ham)))
P=dict()
len_s=len(spam)
len_h=len(ham)

for word in list(set(spam+ham)):

    P[word]=[]
    P[word].append((spam.count(word)+1.0)/(len_s+V))
    P[word].append((ham.count(word)+1.0)/(len_h+V))

f=open("data/nbdata.json",'w')
json.dump(P,f)
