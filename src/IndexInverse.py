class IndexInverse :
    """Classe pour l'index inverse : 
    -Identifiant
    -Titre
    -url de depart
    -Contenu
    -Urls de sortie
    -Score """
    
    def __init__(self, ident, titre, urlDepart, contenu, list_url_sorti, score) :
        """Constructeur IndexInverse"""
        self.id = ident
        self.titre = titre
        self.urlD = urlDepart
        self.contenu = contenu
        self.list_url = list_url_sorti
        self.score = score

