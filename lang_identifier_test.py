import os,json,sys
from nltk.tokenize import word_tokenize
from nltk import bigrams,trigrams


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


def create_text_profile(filename):

    f=open((os.path.join(os.path.abspath(folder),filename)))
    text=f.read().lower()

    text=text.decode('latin-1')

    text_profile=dict()

    list_grams(text_profile,text)

    return text_profile


def similarity_measure(l1,l2):

    score=0
    for word in l1:
        if word in l2:
            score+=l1[word]-l2[word]
        else:
            score+=1000

    return score


f=open('data/english.json','r')
english=json.load(f)
f.close()

f=open('data/french.json','r')
french=json.load(f)
f.close()

f=open('data/german.json','r')
german=json.load(f)
f.close()

f=open('data/spanish.json','r')
spanish=json.load(f)
f.close()

f=open('data/italian.json','r')
italian=json.load(f)
f.close()

language_profiles=[english,french,german,spanish,italian]
languages=['english','french','german','spanish','italian']

print "Actual language: English"

for folder,subfolders,files in os.walk('data/sample_language/test/english'):

    for filename in files:

        text_profile=create_text_profile(filename)
        min_score=sys.maxint
        pred_lang=''
        for i,language_profile in enumerate(language_profiles):
            similarity=similarity_measure(text_profile,language_profile)
            if similarity<min_score:
                pred_lang=languages[i]
                min_score=similarity

        print filename,":",pred_lang

print "Actual language: French"

for folder,subfolders,files in os.walk('data/sample_language/test/french'):

    for filename in files:

        text_profile=create_text_profile(filename)
        min_score=sys.maxint
        pred_lang=''
        for i,language_profile in enumerate(language_profiles):
            similarity=similarity_measure(text_profile,language_profile)
            if similarity<min_score:
                pred_lang=languages[i]
                min_score=similarity

        print filename,":",pred_lang

print "Actual language: German"

for folder,subfolders,files in os.walk('data/sample_language/test/german'):

    for filename in files:

        text_profile=create_text_profile(filename)
        min_score=sys.maxint
        pred_lang=''
        for i,language_profile in enumerate(language_profiles):
            similarity=similarity_measure(text_profile,language_profile)
            if similarity<min_score:
                pred_lang=languages[i]
                min_score=similarity

        print filename,":",pred_lang

print "Actual language: Italian"

for folder,subfolders,files in os.walk('data/sample_language/test/italian'):

    for filename in files:

        text_profile=create_text_profile(filename)
        min_score=sys.maxint
        pred_lang=''
        for i,language_profile in enumerate(language_profiles):
            similarity=similarity_measure(text_profile,language_profile)
            if similarity<min_score:
                pred_lang=languages[i]
                min_score=similarity

        print filename,":",pred_lang

print "Actual language: Spanish"

for folder,subfolders,files in os.walk('data/sample_language/test/spanish'):

    for filename in files:

        text_profile=create_text_profile(filename)
        min_score=sys.maxint
        pred_lang=''
        for i,language_profile in enumerate(language_profiles):
            similarity=similarity_measure(text_profile,language_profile)
            if similarity<min_score:
                pred_lang=languages[i]
                min_score=similarity

        print filename,":",pred_lang
