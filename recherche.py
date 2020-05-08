import chargerFichier
from operator import attrgetter
import Document as D

#index = chargerFichier.chargerfichier(r'C:\\Users\\alexa\\Documents\\Master\\Algo_Texte\\pages_web\\pages_web\\')
index = chargerFichier.chargerfichier('./pages_web/')

def trie(fichier):
    fichier_trier = sorted(fichier, key=attrgetter("score"), reverse=True)
    return fichier_trier

def recherche(liste_mot, collectionDocument):
	liste = liste_mot.split()
	index_trie = list()
	for document in collectionDocument :
		score = 0
		for var in liste:
			score = score + D.bm_25(D.findStem(var), document, collectionDocument)
		document.score = score
		index_trie.append(document)
	index_trie = trie(index_trie)
	return index_trie

# recherche avec mots qui sont similaire aux mots cherchés
def recherche2(liste_mot, collectionDocument):
	liste = liste_mot.split()
	index_trie = list()
	for document in collectionDocument :
		score = 0
		for var in liste:
			score = score + D.bm_25v2(var, document, collectionDocument)
		document.score = score
		index_trie.append(document)
	index_trie = trie(index_trie)
	return index_trie

def recuperer_liste_page(fichier) :
    for i in range(0, 10) :
        print(fichier[i].contenu)

# calcul la distance entre deux pages
def distancePages(page1, page2):
	d = 0
	contenu1 = page1.contenu
	contenu2 = page2.contenu
	print(contenu1)
	d = d + D.similar(contenu1,contenu2)
	return d

# supprime les pages trop similaires (à finir)
def supprimerPages(collectionDocument):
	for document in collectionDocument:
		for i in collectionDocument:
			if document != i and distancePages(document,i) > 0.75:
				print(document.urlD)

# recherche avec une erreur
test = recherche2("breuvard",index)
for i in test:
	print(i.urlD + ' ' + str(i.score))
	
