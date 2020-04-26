from math import log

def calculTF(terme, document):
    occ = ParcoursNaif(terme, document)
    nbMot = len(document.split())
    tf = occ / nbMot
    return tf
        

def ParcoursNaif(terme, document) :
    occ = 0
    m = len(terme)
    n = len(document)
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
    idf = log(len(collectionDocument)/freq, 2)
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

def norm_log_tf(terme, document):
    occ = ParcoursNaif(terme, document)
    norm_log = 1 + log(occ, 2)
    return norm_log

def bm_25(terme, document, collectionDocument):
    occ = ParcoursNaif(terme, document)
    k1 = 1.3
    b = 0.75
    d = len(document)
    moy = avgdl(collectionDocument)
    idf = calculIDF(terme, collectionDocument)
    form = idf * ((occ * (k1 + 1))/(occ + k1 * (1 - b + b * (len(document)/moy))))
    return form
    
def avgdl(collectionDocument) :
    value = 0
    for i in collectionDocument :
        value = value + len(i)   
    value = value/len(collectionDocument)
    return value