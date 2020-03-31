from bs4 import BeautifulSoup
import os

def chargerFichier(repertoire):
    Index = dict()
    Index = {}
    Path = os.listdir(repertoire)
    for var in Path :
        with open(var, encoding="ISO-8859-1", mode="r") as fp :
            soup = BeautifulSoup(fp, features="html5lib")
            print(var)
    return Index
chargerFichier(r'C:\\Users\\alexa\\Documents\\Master\\Algo_Texte\\pages_web\\pages_web\\')
