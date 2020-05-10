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
	contenu1 = D.retirerBalises(page1.contenu)
	contenu2 = D.retirerBalises(page2.contenu)
	d = d + D.similar(contenu1,contenu2)
	return d

# supprime les pages trop similaires (pas opti)
def supprimerPages(collectionDocument):
	n = 0
	res = set()
	t = len(collectionDocument)
	doc = collectionDocument
	for document1 in doc:
		res.add(document1)
		for document2 in doc:
			if document1 != document2 and document2 not in res:
				# les pages ne sont pas assez proches (75% de similarité entre les deux pages)
				if distancePages(document1,document2) < 0.75:
					#print("pages non similaires : " + document1.urlD.replace('./pages_web/','') + " " + document2.urlD.replace('./pages_web/',''))
					pass
				# les pages sont trop proches
				else:
					#print("pages similaires : " + document1.urlD.replace('./pages_web/','') + " " + document2.urlD.replace('./pages_web/',''))
					doc.remove(document2)
					#print("page : " + document2.urlD.replace('./pages_web/','') + " supprimé")
				n = n+1
				#print(distancePages(document1,document2))
	print(str(t-len(res)) + ' pages supprimés')
	print("Nombres de comparaisons : " + str(n))
	return list(res)
	
	
# test supprimerPages
new_index = supprimerPages(index)
for i in new_index:
	print(i.urlD.replace('./pages_web/',''))

# recherche avec une erreur
test = recherche2("breuvatr",index)
print("Résultat de la recherche\n")
for i in test:
	print(str(i.urlD.replace('./pages_web/','')) + ' ' + str(i.score))