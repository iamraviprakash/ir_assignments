import os,json
from nltk.tokenize import word_tokenize
from nltk import bigrams,trigrams
import nltk
nltk.data.path.append("/Users/yashsrivastava/Documents/Files/IR/nltk_data")

english=dict()
french=dict()
german=dict()
italian=dict()
spanish=dict()


def list_grams(language,text):

    words=word_tokenize(text)

    for text in words:
        if text.isalnum():

            for bigram in bigrams(text):

                bigram=(''.join(bigram))

                if bigram in language:
                    language[bigram]+=1
                elif bigram not in language:
                    language[bigram]=1

            for trigram in trigrams(text):

                trigram=(''.join(trigram))

                if trigram in language:
                    language[trigram]+=1
                elif trigram not in language:
                    language[trigram]=1


def create_language_profile(language):

    for folder,subfolders,files in os.walk('data/sample_language/train/'+language):

        for filename in files:

            f=open((os.path.join(os.path.abspath(folder),filename)))
            text=f.read().lower()

            global english
            global french
            global german
            global italian
            global spanish

            text=text.decode('latin-1')

            if language=='english':
                list_grams(english,text)
            elif language=='french':
                list_grams(french,text)
            elif language=='german':
                list_grams(german,text)
            elif language=='italian':
                list_grams(italian,text)
            elif language=='spanish':
                list_grams(spanish,text)


create_language_profile('english')
f=open('data/english.json','w')
json.dump(english,f)
f.close()

create_language_profile('french')
f=open('data/french.json','w')
json.dump(french,f)
f.close()

create_language_profile('german')
f=open('data/german.json','w')
json.dump(german,f)
f.close()

create_language_profile('italian')
f=open('data/italian.json','w')
json.dump(italian,f)
f.close()

create_language_profile('spanish')
f=open('data/spanish.json','w')
json.dump(spanish,f)
f.close()
