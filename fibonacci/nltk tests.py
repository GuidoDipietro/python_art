# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:11:56 2019

@author: dipie
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
#from bs4 import BeautifulSoup
#import urllib.request
from operator import itemgetter
from sampleText import text_4 as texto
import time

start = time.time()
stemmer = SnowballStemmer('spanish')

"""
response = urllib.request.urlopen('http://laspreguntasdeguido.blogspot.com/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
"""

#Get tokens from text
tokens = texto.split()

#Delete stupid tokens
clean_tokens = tokens[:]
sr = stopwords.words('spanish')
for token in tokens:
    if token in stopwords.words('spanish') or not(token.isalpha()):
        clean_tokens.remove(token)
        
#Stemming
#Delete this to see how results change... quite a lot
clean_tokens = [stemmer.stem(x) for x in clean_tokens]

#Data printing
freq = nltk.FreqDist(clean_tokens)
words = list(sorted(freq.items(),key=itemgetter(1),reverse=True))
print([x[0] for x in words[:15]])
freq.plot(20, cumulative=False)

#Done
print(time.time() - start)