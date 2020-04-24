import numpy as np

def calculTF(terme, document):
    occ = ParcoursNaif(terme, document)
    nbMot = len(document.split())
    tf = occ / nbMot
    return tf
        

def ParcoursNaif(terme, document) :
    occ = 0
    n = len(terme)
    m = len(document)
    for i in range(0, n-m+1):
        j = 1
        while (j < m and comparer_lettre(document[i+j], terme[j])) :
            j = j+1
        if (j == m) :
            occ = occ + 1
    return occ
    

def comparer_lettre (c1, c2) :
    if (c1 == c2) :
        return 1
    else :
        return 0

def calculIDF(terme, collectionDocument) :
    freq = freqDocument(terme, collectionDocument)
    idf = np.log2(1/freq)
    return idf

def freqDocument(terme, collectionDocument):
    freq = 0
    for i in collectionDocument:
        if (ParcoursNaif(terme, i) != 0):
            freq = freq + 1
    freq2 = freq/len(collectionDocument)
    return freq2

def calculTFIDF(terme, collectionDocument, document):
    tf = calculTF(terme, document)
    idf = calculIDF(terme, collectionDocument)
    tf_idf = tf*idf
    return tf_idf
