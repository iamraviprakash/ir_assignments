import os,json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

f=open('data/nbdata.json','r')
P=json.load(f)
f.close()

spam_count=0
ham_count=0
total_count=0
correct_count=0

for folder,subfolders,files in os.walk('data/sample/test/spam'):
    for filename in files:
        spam_count+=1
        total_count+=1

for folder,subfolders,files in os.walk('data/sample/test/ham'):
    for filename in files:
        ham_count+=1
        total_count+=1

print "Spam documents:"

for folder,subfolders,files in os.walk('data/sample/test/spam'):

    for filename in files:

        P_spam=float(spam_count)/total_count
        P_ham=float(ham_count)/total_count

        f=open((os.path.join(os.path.abspath(folder),filename)))
        for word in word_tokenize(f.read().lower()):
            if word in P:
                P_spam*=P[word][0]
                P_ham*=P[word][1]

        if P_spam>=P_ham:
            correct_count+=1
            print "Spam!"
        else:
            print "Ham!"

print "Ham documents:"

for folder,subfolders,files in os.walk('data/sample/test/ham'):

    for filename in files:

        P_spam=float(spam_count)/total_count
        P_ham=float(ham_count)/total_count

        f=open((os.path.join(os.path.abspath(folder),filename)))
        for word in word_tokenize(f.read().lower()):
            if word in P:
                P_spam*=P[word][0]
                P_ham*=P[word][1]

        if P_spam>=P_ham:
            print "Spam!"
        else:
            correct_count+=1
            print "Ham!"

print "Accuracy:",float(correct_count)/total_count
