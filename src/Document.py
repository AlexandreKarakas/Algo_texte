from math import log

def calculTF(terme, document):
    occ = ParcoursNaif(terme, document.contenu)
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
    if (freq == 0) :
        return 0
    else :
        idf = log(len(collectionDocument)/freq,2)
        return idf

def freqDocument(terme, collectionDocument):
    freq = 0
    for i in collectionDocument:
        if (ParcoursNaif(terme, i.contenu) != 0):
            freq = freq + 1
    return freq

def calculTFIDF(terme, collectionDocument, document):
    tf = calculTF(terme, document)
    idf = calculIDF(terme, collectionDocument)
    tf_idf = tf*idf
    return tf_idf

def norm_log_tf(terme, document):
    occ = ParcoursNaif(terme, document.contenu)
    norm_log = 1 + log(occ, 2)
    return norm_log

def bm_25(terme, document, collectionDocument):
    occ = ParcoursNaif(terme, document.contenu)
    k1 = 1.3
    b = 0.75
    moy = avgdl(collectionDocument)
    idf = calculIDF(terme, collectionDocument)
    form = idf * ((occ * (k1 + 1))/(occ + k1 * (1 - b + b * (len(document.contenu)/moy))))
    return form

def avgdl(collectionDocument) :
    value = 0
    for i in collectionDocument :
        value = value + len(i.contenu)   
    value = value/len(collectionDocument)
    return value

def avgdl_and_idf(terme, collectionDocument):
    value = 0
    freq = 0
    for i in collectionDocument :
        value = value + len(i.contenu)
        if (ParcoursNaif(terme, i.contenu) != 0):
            freq = freq + 1
    value = value/len(collectionDocument)
    if (freq == 0) :
        liste = [value, 0]
        return liste
    else :
        idf = log(len(collectionDocument)/freq,2)
        liste = [value, idf]
        return liste

def bm_25_opti(terme, document, collectionDocument):
    occ = ParcoursNaif(terme, document.contenu)
    k1 = 1.3
    b = 0.75
    liste = avgdl_and_idf(terme, collectionDocument)
    moy = liste[0]
    idf = liste[1]
    form = idf * ((occ * (k1 + 1))/(occ + k1 * (1 - b + b * (len(document.contenu)/moy))))
    return form