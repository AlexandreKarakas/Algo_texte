import chargerFichier
from operator import attrgetter
import Document as D

index = chargerFichier.chargerfichier(r'C:\\Users\\alexa\\Documents\\Master\\Algo_Texte\\pages_web\\pages_web\\')

def trie(fichier):
    fichier_trier = sorted(fichier, key=attrgetter("score"))
    return fichier_trier

def recherche(liste_mot, collectionDocument):
    liste = liste_mot.split()
    index_trie = list()
    for document in collectionDocument :
        score = 0
        for var in liste:
            score = score + D.bm_25(var, document, collectionDocument)
        document.score = score
        index_trie.append(document)
        print(score)
recherche("vérification", index)