"""Module d'encodage de chaînes de caractères avec algorithmes itératif et récursif."""

# Imports
import sys
sys.setrecursionlimit(2000)  # Permet de traiter des chaînes longues dans la fonction récursive

#### Fonctions secondaires

def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée
    en argument selon un algorithme itératif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: La liste des tuples (caractère, nombre d'occurrences).
    """
    # Initialisation des listes pour stocker les caractères uniques et leurs occurrences
    C = [s[0]]
    O = [1]
    k = 1

    # Parcours de la chaîne
    while k < len(s):
        if s[k] == s[k - 1]:
            O[-1] += 1  # Incrémente le compteur pour le caractère actuel
        else:
            C.append(s[k])  # Ajoute un nouveau caractère à la liste
            O.append(1)  # Initialise son compteur à 1
        k += 1

    # Retourne une liste de tuples (caractère, nombre d'occurrences)
    return list(zip(C, O))

def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée
    en argument selon un algorithme récursif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: La liste des tuples (caractère, nombre d'occurrences).
    """
    # Cas de base : chaîne vide
    if len(s) == 0:
        return []

    # Compte le nombre de caractères identiques au premier
    nb = 1
    while nb < len(s) and s[0] == s[nb]:
        nb += 1

    # Combine le résultat du premier groupe avec l'appel récursif sur le reste
    return [(s[0], nb)] + artcode_r(s[nb:])

#### Fonction principale

def main():
    """Point d'entrée principal du programme."""
    # Exemple d'encodage avec les deux algorithmes
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

# Exécute la fonction principale uniquement si ce script est exécuté directement
if __name__ == "__main__":
    main()
