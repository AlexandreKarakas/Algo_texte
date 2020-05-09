import chargerFichier
from operator import attrgetter
import Document as D
from math import log

index = chargerFichier.chargerfichier(r'C:\\Users\\alexa\\Documents\\Master\\Algo_Texte\\pages_web\\pages_web\\')

def trie(fichier):
    fichier_trier = sorted(fichier, key=attrgetter("score"), reverse=True)
    return fichier_trier

def recherche(liste_mot, collectionDocument):
    liste = liste_mot.split()
    index_trie = list()
    for document in collectionDocument :
        score = 0
        for var in liste:
            score = score + D.bm_25_opti(var, document, collectionDocument)
        document.score = score
        index_trie.append(document)
    index_trie = trie(index_trie)
    return index_trie

#A n'utiliser que pour le debug ou si le programme est trop long

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
        index_trie.append(document)
    index_trie = trie(index_trie)
    return index_trie

def recuperer_liste_page(fichier) :
    for i in range(0, 10) :
        print(fichier[i].contenu)

recherche("breuvart", index)