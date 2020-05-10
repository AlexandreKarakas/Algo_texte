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
	#moyenne des longueurs des documents de la collection
    moy = D.avgdl(collectionDocument)
    liste = liste_mot.split()
    index_trie = list()
    idf = list()
    #Charge les idf pour chaque mots clés
    for var in liste:
        idf.append(D.calculIDF(var, collectionDocument))
    for document in collectionDocument :
        i = 0
        score = 0
        for var in liste:
            score = score + D.bm_25(var, document, moy, idf[i])
            i = i + 1
        document.score = score
        if score > 0:
            index_trie.append(document)
    index_trie = trie(index_trie)
    return index_trie

# recherche avec mots qui sont similaire aux mots cherchés
def recherche2(liste_mot, collectionDocument):
    #moyenne des longueurs des documents de la collection
	moy = D.avgdl(collectionDocument)
	liste = liste_mot.split()
	index_trie = list()
	idf = list()
	#Charge les idf pour chaque mots clés
	for var in liste:
		idf.append(D.calculIDF(var, collectionDocument))
	for document in collectionDocument :
		i = 0
		score = 0
		for var in liste:
			score = score + D.bm_25v2(var, document, moy, idf[i])
		document.score = score
		if score > 0:	
			index_trie.append(document)
	index_trie = trie(index_trie)
	return index_trie

def getTop10pages(index_trie):
    return index_trie[:10]

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
	
# mots proches du mots cherché
def motsProches(mot, collectionDocument):
	liste = mot.split()
	mots = set()
	for document in collectionDocument:
		for mot in liste:
			contenu = D.retirerBalises(document.contenu).split()
			for i in contenu:
				if (D.similar(mot,i) >= 0.75) or (mot.upper() in i.upper()):
					mots.add(i)
	return mots
	
# test supprimerPages
#index = loadIndex()
#index = supprimerPages(index)
	
# test motsProches
'''test = motsProches("euvar",index)
for i in test:
	print(i)'''

# recherche avec une erreur
'''test = recherche2("breuvatr",index)
for i in test:
	print(i.filename)'''
	
