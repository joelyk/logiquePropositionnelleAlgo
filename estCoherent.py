"""
Estcoherent - Vérification de la cohérence d'un ensemble de clauses.

Auteur: Mr. Joël Yankam
Site Web: [pandacodeur.com](https://www.pandacodeur.com)
"""

def estcoherent(K):
    """
    Vérifie la cohérence d'un ensemble de clauses.

    Cette fonction prend un ensemble de clauses K et vérifie si cet ensemble est cohérent
    en utilisant un algorithme basé sur les règles suivantes :
    1. Si l'ensemble K est vide, il est considéré comme cohérent.
    2. Si la clause '⊥' (faux) est présente dans K, alors l'ensemble est incohérent.
    3. Sinon, l'algorithme sélectionne un symbole propositionnel x à partir d'une clause de K.
    4. Il crée ensuite deux ensembles de clauses en ajoutant x en tant que 'T' et '⊥' respectivement.
    5. Il récursivement vérifie la cohérence avec Kx←T ou Kx←⊥.

    Args:
        K (list): Liste d'ensembles représentant les clauses.

    Returns:
        int: 1 si l'ensemble K est cohérent, 0 sinon.
    """
    # Cas de base : ensemble vide, retourne 1 (cohérent)
    if not K:
        return 1
    # Vérifie si ⊥ (faux) est dans K, retourne 0 (incohérent)
    elif any(clause == set(['⊥']) for clause in K):
        return 0
    else:
        # Choisissez un symbole propositionnel x dans une clause de K
        for clause in K:
            for symbol in clause:
                if symbol != '⊥':
                    x = symbol
                    break

        # Créez deux ensembles de clauses en ajoutant x en tant que T et ⊥
        K_true = [clause.difference({x}) for clause in K]
        K_false = [clause.difference({x}) if x in clause else clause.union({'⊥'}) for clause in K]

        # Récursivement vérifiez la cohérence avec Kx←T ou Kx←⊥
        return estcoherent(K_true) or estcoherent(K_false)

# Jeu de données
K = [{ 'a', 'b', 'c' },
     { '⊥' },
     { '¬a', '¬b', '¬c' },
     { '¬a', 'b', 'c' },
     { 'b', '¬c' },
     { 'a', '¬b', '¬c' },
     { 'c', '¬b' }]

# Appel de la fonction
resultat = estcoherent(K)

# Affichage du résultat
if resultat == 1:
    print("L'ensemble K est cohérent.")
else:
    print("L'ensemble K n'est pas cohérent.")
