import os,json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

spam=[]
ham=[]

for folder,subfolders,files in os.walk('data/sample/spam'):

    for filename in files:

        ip=open((os.path.join(os.path.abspath(folder),filename)),'r')
        final_text=''
        for line in ip:
            line=line.strip().decode("ascii","ignore").encode("ascii")
            if line=="":
                continue
            final_text+=line+'\n'
        ip.close()

        op=open((os.path.join(os.path.abspath(folder),filename)),'w')
        op.write(final_text)
        op.close()

        f=open((os.path.join(os.path.abspath(folder),filename)))
        for word in word_tokenize(f.read().lower()):
            if word.isalnum() and word not in stopwords.words('english') and word!='subject':
                spam.append(word)

        f.close()

for folder,subfolders,files in os.walk('data/sample/ham'):

    for filename in files:

        ip=open((os.path.join(os.path.abspath(folder),filename)),'r')
        final_text=''
        for line in ip:
            line=line.strip().decode("ascii","ignore").encode("ascii")
            if line=="":
                continue
            final_text+=line+'\n'
        ip.close()

        op=open((os.path.join(os.path.abspath(folder),filename)),'w')
        op.write(final_text)
        op.close()

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
