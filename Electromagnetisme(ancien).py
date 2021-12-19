
import math as m
import CONSTANTES as C





"""
Hypothèses: Xi_e = Xi_m (meilleur cas) et Xi_m = dm (TODO car faux) 
"""
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
        # self.P = self.calcul_puissance()    # calculé avec la formule 2.39 en disant que Xi_m = Xi_i(meilleur cas) (doc uv) (pas pour mtn pcq on va calculer le dumping électrique
        self.N = self.nombre_spires()   # calculé a partir du produit des 2 équations en 2.25
        self.de = self.calcul_de()  # calcul de "de" à partir du N trouvé

    def calcul_resistance_m(self):
        """

        :return: dictionnaire avec pour chaque fil un tuple(rayon, résistance par mètre)
        """
        dico_fils = {}
        for rayon in self.rayons_fils:
            r = self.resistivite / (self.rayons_fils[rayon][0] / 1000) ** 2 * m.pi
            dico_fils[rayon] = (self.rayons_fils[rayon][0], r)

        return dico_fils

    def calcul_de(self):
        """
        calcul de "de" en fonction de N
        :return: lsite avec des tuples (de, N, nom du fil, longueur de la bobine)
        """
        de_l = []
        for l in self.N:
            N = l[0]  # adimentionnel
            fil = l[1]  # str
            epaisseur_bobine = l[2] 
            largeur_bobine = l[3]
            kt = N * self.B * (largeur_bobine / 1000)  # l / 1000 pour mettre en mètres
            Rcoil = N * m.pi * epaisseur_bobine * self.dico_fils[fil][1] / 1000
            Rload = Rcoil + ((kt ** 2) / self.Xi_m)
            de = (kt ** 2) / (Rcoil + Rload)
            de_l.append((de, N, fil, epaisseur_bobine))
        return de_l

    def resultat(self):
        """
        trouve le bon nombre de spires pour avoir une puissance la plus puissante possible
        :return: résultat
        """
        best_p = 0
        for l in self.de:
            de = l[0]
            N = l[1]
            fil = l[2]
            epaisseur_bobine = l[3]
            P = (self.m ** 2 * de * omega_n ** 4 * self.A ** 2) / (2 * (de + self.Xi_m) ** 2)
            if P > best_p:
                best_p = P
                best = (fil, N, de, P, epaisseur_bobine)
        print(f" fil idéal: {best[0]}, nombre de spires: {best[1]}, longueur de la bobine: {self.hcoil} mm, rayon de la bobine: {self.Ri} mm, \n" \
              f", puissance avec notre bobine: {best[3]}, épaisseur de la conche " \
              f"de fil sur la bobine: {epaisseur_bobine} mm. ")

    """
    A faire plus tard
    def calcul_puissance(self):
        #calcule la puissance (éq 2.39)
        
        return (self.m * self.omega_n ** 3 * self.A ** 2) / (16 * self.Xi_m)
"""
    def nombre_spires(self):
        """
        calcule le nombre de sprires (eq 2.25)
        !!!! choix des bornes des "range" choisies de manière arbitraire !!!!
        (ça change en fonction du choix mais il faut qu'il soit réalisabe)
        :return: liste avec des tuples(nombres de sprires, fil, épaisseur de la bobine, longueur de la bobine)
        """
        liste = []
        for fil in self.dico_fils:
            diam = self.dico_fils[fil][0] * 2
            Ri = 20
            for Ro in range(Ri + 1, Ri + self.Ro_max):    # mm
                epaisseur_bobine = Ro - Ri
                l = Ro + Ri
                N = (4 * self.hcoil * epaisseur_bobine) / (diam ** 2 * (m.pi / self.k_co))
                liste.append((N, fil, epaisseur_bobine, l))

        return liste


