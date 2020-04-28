from bs4 import BeautifulSoup
import os
import IndexInverse
import Document
import pickle
import sys

sys.setrecursionlimit(10**8)
def chargerfichier(repertoire):
    index = list()
    Path = os.listdir(repertoire)
    for var in Path :
        var = repertoire + var
        with open(var, encoding="ISO-8859-1", mode="r") as fp :
            soup = BeautifulSoup(fp, features="html5lib")
            titre = soup.title
            contenu = str(soup.find_all('body'))
            url = soup.find_all('a')
            inv = IndexInverse.IndexInverse(titre, var, contenu, url, 0)
            index.append(inv)   
    fp.close()
    return index

