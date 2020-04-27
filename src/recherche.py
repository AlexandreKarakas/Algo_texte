import chargerFichier
from operator import attrgetter

index = chargerFichier.chargerfichier(r'C:\\Users\\alexa\\Documents\\Master\\Algo_Texte\\pages_web\\pages_web\\')

def trie(fichier):
    fichier_trier = sorted(fichier, key=attrgetter("score"))
    return fichier_trier

index = trie(index.values())
print(index)