# logiquePropositionnelleAlgo
# Vérification de la Cohérence d'un Ensemble de Clauses


## Auteur
- Joël Yankam
- Site Web : [pandacodeur.com](https://www.pandacodeur.com)
- Lien Exercice : 

## Description
Ce code Python permet de vérifier la cohérence d'un ensemble de clauses en utilisant un algorithme basé sur les règles logiques. Vous pouvez utiliser cet outil pour déterminer si un ensemble donné de clauses est cohérent ou non, faudra bien sur changer la base de connaissance.

## Fonctionnement
L'algorithme de vérification de cohérence suit les règles suivantes :
1. Si l'ensemble de clauses est vide, il est considéré comme cohérent.
2. Si la clause '⊥' (faux) est présente dans l'ensemble de clauses, alors l'ensemble est incohérent.
3. Sinon, l'algorithme sélectionne un symbole propositionnel x à partir d'une clause de l'ensemble.
4. Il crée ensuite deux ensembles de clauses en ajoutant x en tant que 'T' et '⊥' respectivement.
5. Il récursivement vérifie la cohérence avec Kx←T ou Kx←⊥.

## Utilisation
```python
# Jeu de données (exemples)
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
