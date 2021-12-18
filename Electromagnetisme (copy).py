
import math as m
import CONSTANTES as C





#Rload = résistance à rajouter



class ElectroMec:

    def __init__(self):
        self.rayons_fils = C.rayons_fils  # Donée fablab
        self.resistivite = C.resistivite_cuivre
        self.dico_fils = self.calcul_resistance_m()  # résistance calculée grâce à: https://www.positron-libre.com/cours/tableaux-formulaires/tableau-resistance-fil-cuivre.php
        self.longueur = C.COTE_AIMANT  # Données techniques aimant
        self.epaisseur = C.EPAISSEUR_AIMANT  # idem
        self.B = C.B
        self.hcoil = C.LONGUEUR_BOBINE
        self.Ri = C.RAYON_BOBINE
        self.Ro_max = C.EPAISSEUR_BOBINE_MAX
        self.omega_n = C.FREQUENCE_PROPRE_TABLE  # omega calculé dans partie oscillation
        self.A = C.AMPLITUDE  # amplitude du mouvement de la table
        self.Xi_m = C.Xi_m    # valeur a déterminer expérimentalement(à changer dans CONSTANTES.py)
        self.k_co = C.k_co    # trouvé page 22 dans https://uv.ulb.ac.be/pluginfile.php/3273876/mod_resource/content/2/Calcul_puissance_harvester.pdf
        self.m = C.MASSE  #   A déterminer, à changer dans COUNSTANTES
        self.dm =  self.calcul_dm()

    def calcul_resistance_m(self):
        """

        :return: dictionnaire avec pour chaque fil un tuple(rayon, résistance par mètre)
        """
        dico_fils = {}
        for rayon in self.rayons_fils:
            r = self.resistivite / (self.rayons_fils[rayon][0] / 1000) ** 2 * m.pi
            dico_fils[rayon] = (self.rayons_fils[rayon][0], r)

        return dico_fils

    def calcul_dm(self):
        """
        dm = d dans formules 
        """

    
    
    
    
    
    
    def puissance_max(self):
        """
        Calcule la puissance maximale possible: lorsque de = dm 
        """
        return (self.masse ** 2 * self.omega_n ** 4 * self.A ** 2) / (8 * self.dm)  # formule 2.39

  
