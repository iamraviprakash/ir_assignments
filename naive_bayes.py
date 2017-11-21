import os

spam=[]
ham=[]

for folder,subfolders,files in os.walk('data/enron1/spam'):

    for filename in files:
        f=open((os.path.join(os.path.abspath(folder),filename)))
        for word in word_tokenize(f.read().lower()):
            if word.isalnum() and word not in stopwords.words('english') and word!='subject':
                spam.append(word)

for folder,subfolders,files in os.walk('data/enron1/ham'):

    for filename in files:
        f=open((os.path.join(os.path.abspath(folder),filename)))
        for word in word_tokenize(f.read().lower()):
            if word.isalnum() and word not in stopwords.words('english') and word!='subject':
                ham.append(word)

spam=list(set(spam))
ham=list(set(ham))
