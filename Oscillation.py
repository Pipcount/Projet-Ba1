import CONSTANTES as C


class Oscilliation:
    """
    Calcule la longueur idéale de la poutre et la fréquence naturelle correspondante
    """
    def __init__(self):
        self.young = C.MOD_YOUNG
        self.epaisseur = C.EPAISSEUR_POUTRE
        self.largeur = C.LARGEUR_POUTRE
        self.inertie = C.INERTIE
        self.omega = C.FREQUENCE_PROPRE_TABLE
        self.masse = C.MASSE
        self.longueur_poutre = self.longueur_poutre_id()
        self.omega_n = self.calcul_omega_n()


    def longueur_poutre_id(self):
        return ((3 * self.young * self.inertie) / (self.omega ** 2 * self.masse)) ** (1/3)
 
    
    def longueur_poutre_res(self):
        """
        Ecrit le résultat de la longueur idéale de poutre
        :return: str 
        """
        print(f"longueur de la poutre optimale: {self.longueur_poutre * 100} cm\n")







