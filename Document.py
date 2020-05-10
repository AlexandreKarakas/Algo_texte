# -*- coding: utf-8 -*-

import re
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import FrenchStemmer
from math import log
from difflib import SequenceMatcher

# Renvoie un float entre 0 et 1 qui correspond à la similarité entre les mots
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    
# Retire les balises dans un texte
def retirerBalises(text):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', text)
	return cleantext

def calculTF(terme, document):
    occ = ParcoursNaif(terme, document.contenu)
    nbMot = len(document.split())
    tf = occ / nbMot
    return tf

def ParcoursNaif(terme, document) :
    occ = 0
    m = len(terme)
    n = len(document)
    for i in range(0, n-m+1):
        j = 1
        while (j < m and comparer_lettre(document[i+j-1], terme[j-1])) :
            j = j+1
        if (j == m) :
            occ = occ + 1
    return occ

def ParcoursNaif2(terme, document) :
    occ = 0
    racine = findStem(terme)
    tmp = document.split()
    for i in tmp:
        if racine in retirerBalises(i):
            occ = occ + 1
        elif similar(racine, retirerBalises(i)) >= 0.75:
            occ = occ + similar(racine, retirerBalises(i))
    return occ
   
def comparer_lettre (c1, c2) :
    if (c1 == c2) :
        return 1
    else :
        return 0

def calculIDF(terme, collectionDocument) :
    freq = freqDocument(terme, collectionDocument)
    if (freq == 0) :
        return 0
    else :
        idf = log(len(collectionDocument)/freq,2)
        return idf

def freqDocument(terme, collectionDocument):
    freq = 0
    for i in collectionDocument:
        if (ParcoursNaif2(terme, i.contenu) != 0):
            freq = freq + 1
    return freq

def calculTFIDF(terme, collectionDocument, document):
    tf = calculTF(terme, document)
    idf = calculIDF(terme, collectionDocument)
    tf_idf = tf*idf
    return tf_idf

def norm_log_tf(terme, document):
    occ = ParcoursNaif(terme, document.contenu)
    norm_log = 1 + log(occ, 2)
    return norm_log

def bm_25(terme, document, collectionDocument):
    occ = ParcoursNaif(terme, document.contenu)
    k1 = 1.3
    b = 0.75
    moy = avgdl(collectionDocument)
    idf = calculIDF(terme, collectionDocument)
    form = idf * ((occ * (k1 + 1))/(occ + k1 * (1 - b + b * (len(document.contenu)/moy))))
    return form
    
def bm_25v2(terme, document, collectionDocument):
    occ = ParcoursNaif2(terme, retirerBalises(document.contenu))
    k1 = 1.3
    b = 0.75
    moy = avgdl(collectionDocument)
    idf = calculIDF(terme, collectionDocument)
    form = idf * ((occ * (k1 + 1))/(occ + k1 * (1 - b + b * (len(document.contenu)/moy))))
    return form

def avgdl(collectionDocument) :
    value = 0
    for i in collectionDocument :
        value = value + len(i.contenu)   
    value = value/len(collectionDocument)
    return value
    
# Tokenize un texte
def tokenizeSent(phrase):
	return sent_tokenize(phrase)
	
# Tokenize un texte
def tokenizeWord(phrase):
	return word_tokenize(phrase)
	
# Enlève les mots inutiles dans un texte (Ex: le, la, de, du, etc.)
def nettoyerPhrase(phrases):
	res = []
	stop_words = set(stopwords.words("french"))
	for phrase in tokenizeSent(phrases):
		for mot in tokenizeWord(phrase):
			if mot not in stop_words:
				res.append(mot)
	return res

# Renvoie une forme canonique du mot
def findStem(mot):
	stemmer = FrenchStemmer()
	return stemmer.stem(mot)
