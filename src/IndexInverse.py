class IndexInverse :
    """Classe pour l'index inverse : 
    -Identifiant
    -Titre
    -url de depart
    -Contenu
    -Urls de sortie
    -Score """
    
    def __init__(self, titre, urlDepart, contenu, list_url_sorti, score) :
        """Constructeur IndexInverse"""
        self.titre = titre
        self.urlD = urlDepart
        self.contenu = contenu
        self.list_url = list_url_sorti
        self.score = score

