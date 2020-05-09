import chargerFichier
from operator import attrgetter
import Document as D
from nltk.probability import FreqDist

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
			score = score + D.bm_25(var, document, collectionDocument)
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
	d = d + D.similar(contenu1,contenu2)
	return d

# supprime les pages trop similaires (pas opti)
def supprimerPages(collectionDocument):
	res = set()
	t = len(collectionDocument)
	doc = collectionDocument
	for document1 in doc:
		for document2 in doc:
			if document1 != document2:
				# les pages ne sont pas assez proches (75% de similarité entre les deux pages)
				if distancePages(document1,document2) < 0.75:
					res.add(document1)
				# les pages sont trop proches
				else:
					doc.remove(document2)
	print(str(t-len(res)) + ' pages supprimés')
	return list(res)
	
# test supprimerPages
new_index = supprimerPages(index)
for i in new_index:
	print(i.urlD)

# recherche avec une erreur
test = recherche2("breuvard",index)
for i in test:
	print(i.urlD + ' ' + str(i.score))
	
	
