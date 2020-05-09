import sys, os
import chargerFichier as cf
from operator import attrgetter
import Document as D

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

def getTop10pages(index_trie):
    return index_trie[:10]
