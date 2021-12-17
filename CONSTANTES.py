import math as m

""" Caractéristiques table vibrante et poutre """

FREQUENCE = 5  # f représente la frequence qui vaut 5 hertz
AMPLITUDE = 0.006  # valeur de l'amplitude en mètre

""" Caractéristiques poutre """

MOD_YOUNG = 65 * 10 ** 9  # module de young(ici alu pour ex)(calculé rapport)
EPAISSEUR_POUTRE = 0.001  # Epaisseur de la poutre en mètres
LARGEUR_POUTRE = 0.021  # Largeur de la poutre en mètres
INERTIE = (LARGEUR_POUTRE * EPAISSEUR_POUTRE ** 3) / 12  # inetrie de la poutre
FREQUENCE_PROPRE_TABLE = 2 * m.pi * FREQUENCE  # w
MASSE = 0.1  # en kg
""" caractéristique bobine """

rayons_fils = {"fil_1": (0.5,), "fil_2": (0.6,), "fil_3": (0.2,), "fil_4": (0.06,), "fil_5": (0.1,), "fil_6": (0.4,), "fil_7": (0.75,)}
# en mm

MASSE_VOL_FIL = 8960  # kg/m3

k_co = 0.6  # doc harvester
resistivite_cuivre = 1.725 * 10 ** (-8)
LONGUEUR_BOBINE = 35  # mm
RAYON_BOBINE = 10  # mm
EPAISSEUR_BOBINE_MAX = 10   # mm

""" amortissement """

Xi_m = 0.036862

"""  magnétisme  """


COTE_AIMANT = 0.04  # côté de l'aimant
EPAISSEUR_AIMANT = 0.004  # Epaisseur de l'aimant
B = 540 * 10 ** (-4)    # Valeur p-e à changer
