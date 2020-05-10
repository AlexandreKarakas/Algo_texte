from bs4 import BeautifulSoup
import os

def Indexation(repertoire):
    Index = dict()
    Index = {}
    Path = os.listdir(repertoire)
    for var in Path :
        with open(var, encoding="unicode_escape") as fp :
            soup = BeautifulSoup(fp)
        #print(soup.prettify())

Indexation('D:\Téléchargements\pages_web')
