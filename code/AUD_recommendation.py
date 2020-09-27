import spacy
import pandas as pd
import numpy as np



from spacy.lang.en import English
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import random


spacy.load("en_core_web_sm")

#clean our texts and return a list of tokens
parser = English()
def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens



#find the meanings of words, synonyms, antonyms, and more
nltk.download('wordnet')
from nltk.corpus import wordnet as wn


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


#Filter out stop words:
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))



#define a function to prepare the text for topic modelling:
def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens



#apply those function

data = pd.read_csv("/Users/sognoneve/Desktop/Unstra Data/FinalProject/pppp.csv")
data['Arrival'] = data.Title + ' ' + data.Text
text_data=[]
# with open(data1) as f:
for line in data['Arrival']:
    tokens = prepare_text_for_lda(line)
    text_data.append(tokens)

data['key']=text_data

userinput = []
crit = False
while crit == False:
    inp = input("Enter the key word and enter the True if you end: ")
    if inp == 'True':
        crit = True
    else:
        userinput.append(inp.lower())

num = []

for j in text_data:
    count = 0
    for i in userinput:
        if i in j:
            count = count + 1
    perc = count / len(userinput)
    num.append(perc)

data['match'] = num



d1=data.sort_values(by=['match'],ascending=False)
d1['url'].head(5)
