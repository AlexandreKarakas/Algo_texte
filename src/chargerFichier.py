from bs4 import BeautifulSoup
import os
import IndexInverse
import Document

def chargerFichier(repertoire):
    index = dict()
    Path = os.listdir(repertoire)
    ident = 0
    for var in Path :
        var = 'C:\\Users\\alexa\\Documents\\Master\\Algo_Texte\\pages_web\\pages_web\\' + var
        with open(var, encoding="ISO-8859-1", mode="r") as fp :
            soup = BeautifulSoup(fp, features="html5lib")
            titre = soup.title
            contenu = soup.body
            url = soup.find_all('a')
            inv = IndexInverse.IndexInverse(titre, var, contenu, url, 0)
            index[ident] = inv
            ident = ident + 1
    return index
    


chargerFichier(r'C:\\Users\\alexa\\Documents\\Master\\Algo_Texte\\pages_web\\pages_web\\')
