
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
        self.m = C.MASSE  #   A déterminer, à changer dans COUNSTANTES
        self.hcoil = 0.035 # en m
        self.dm = C.dm


    def calcul_resistance_m(self):
        """

        :return: dictionnaire avec pour chaque fil un tuple(rayon, résistance par mètre)
        """
        dico_fils = {}
        for rayon in self.rayons_fils:
            r = self.resistivite / (self.rayons_fils[rayon][0] / 1000) ** 2 * m.pi
            dico_fils[rayon] = (self.rayons_fils[rayon][0], r)

        return dico_fils

    
    def calcul_N(self):
        """
        Eq 1 : N = self.hcoil * (Ro - Ri) / ((self.dico_fils[fil][0] * 2) ** 2)
        Eq 2 : Rc = N * m.pi * (Ro - Ri) * self.dico_fils[fil][1]
        Eq 3 : Rl = Rc + (N * self.B * (Ro + ri)) ** 2) / self.dm
        Eq 4 : de = self.dm = ((N * self.B * (Ro + ri)) ** 2) / (Rc + Rl)

        """
        res = ""
        borne = 100
        for fil in self.dico_fils:
            for Ri_mm in range(1, 20):
                Ri = Ri_mm / 1000 #pour mettre en mètres
                for Ro_mm in range(1, 41):
                    Ro = Ro_mm / 1000  #pour mettre en mètres
                    if Ro != Ri:
                        N = self.hcoil * (Ro - Ri) / ((self.dico_fils[fil][0] / 500) ** 2)  #eq 1
                        Rc = N * m.pi * (Ro - Ri) * self.dico_fils[fil][1]  #eq 
                        Rl = Rc + ((N * self.B * (Ro + Ri)) ** 2) / self.dm  # eq 3
                        de = ((N * self.B * (Ro + Ri)) ** 2) / (Rc + Rl)  # eq 4
                        comp = abs(de - self.dm) # on regarde si de es t proche de dm 
                        if comp < borne:
                            res = ""
                            borne = comp
                            res = f"fil : {fil}, Ri : {Ri}, Ro : {Ro}, Rc : {Rc}, Rl = {Rl}, nombre de spires : {N}"
        return res

   
    
    def puissance_max(self):
        """
        Calcule la puissance maximale possible: lorsque de = dm 
        """
        return (self.masse ** 2 * self.omega_n ** 4 * self.A ** 2) / (8 * self.dm)  # formule 2.39

  



