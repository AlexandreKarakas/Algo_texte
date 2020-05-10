import sys, os
import chargerFichier as cf
from operator import attrgetter
import Document as D
from math import log

def loadIndex():
    index = cf.chargerfichier(os.path.join(sys.path[0],'static','pages_web',''))
    return index

def trie(fichier):
    fichier_trier = sorted(fichier, key=attrgetter("score"), reverse=True)
    return fichier_trier

def recherche(liste_mot, collectionDocument):
    liste = liste_mot.split()
    index_trie = list()
    for document in collectionDocument :
        score = 0
        for var in liste:
            score = score + D.bm_25(var, document, collectionDocument)
        document.score = score
        if(score > 0):
            index_trie.append(document)
    index_trie = trie(index_trie)
    return index_trie
    
def recherche_debug(liste_mot, collectionDocument):
    liste = liste_mot.split()
    index_trie = list()
    value = 0
    freq = 0
    for document in collectionDocument :
        score = 0
        for var in liste:
            occ = D.ParcoursNaif(var, document.contenu)
            k1 = 1.3
            b = 0.75
            value = value + len(document.contenu)
            if (occ != 0):
                freq = freq + 1
            value = value/len(collectionDocument)
            if (freq == 0) :
                idf = 0
            else :
                idf = log(len(collectionDocument)/freq,2)
            moy = value
            form = idf * ((occ * (k1 + 1))/(occ + k1 * (1 - b + b * (len(document.contenu)/moy))))
            score = score + form
        document.score = score
        if(score > 0):
            index_trie.append(document)
    index_trie = trie(index_trie)
    return index_trie

def getTop10pages(index_trie):
    return index_trie[:10]
