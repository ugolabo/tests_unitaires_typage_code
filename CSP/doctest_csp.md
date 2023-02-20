# Tester le module csp.py

    >>> import csp_v2 as script

## Classe `CSP`, constructeur `__init__()`

Créer une instance.

    >>> csp = script.CSP([1, 2, 3, 4], {1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]})
    >>> csp2 = script.CSP([1, 2, 3, 4, 5],{1: [1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5], 3: [1, 2, 3, 4, 5], 4: [1, 2, 3, 4, 5], 5: [1, 2, 3, 4, 5]})

Tests.

    >>> csp.variables
    [1, 2, 3, 4]

    >>> csp2.variables
    [1, 2, 3, 4, 5]

    >>> csp.domains
    {1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]}

    >>> csp2.domains
    {1: [1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5], 3: [1, 2, 3, 4, 5], 4: [1, 2, 3, 4, 5], 5: [1, 2, 3, 4, 5]}

    >>> csp.constraints
    {1: [], 2: [], 3: [], 4: []}

    >>> csp2.constraints
    {1: [], 2: [], 3: [], 4: [], 5: []}

## Classe `CSP`, méthode `add_constraint`()

Créer une instance.

    >>> from queens_v2 import QueensConstraint

    >>> csp = script.CSP([1, 2, 3, 4], {1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]})
    >>> csp2 = script.CSP([1, 2, 3, 4, 5],{1: [1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5], 3: [1, 2, 3, 4, 5], 4: [1, 2, 3, 4, 5], 5: [1, 2, 3, 4, 5]})

Tests.

    >>> csp.add_constraint(QueensConstraint([1, 2, 3, 4]))
    >>> len(csp.constraints)
    4

    >>> csp2.add_constraint(QueensConstraint([1, 2, 3, 4, 5]))
    >>> len(csp2.constraints)
    5

## Classe `CSP`, méthode `consistent()`

Créer une instance.

    >>> csp = script.CSP([1, 2, 3, 4], {1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]})

`consistent()` parcourt toutes les contraintes pour une variable donnée
(ce sera toujours la variable qui vient d'être ajoutée à l'affectation) et
vérifie si la contrainte est satisfaite, 
étant donné la nouvelle affectation.
Si l'affectation satisfait toutes les contraintes: `True`.
Si une contrainte imposée à la variable n'est pas satisfaite: `False`.
Ce cadre de satisfaction de contraintes utilisera une simple recherche de
retour en arrière pour trouver
la solution aux problèmes.
Le retour en arrière est l'idée qu'une fois que vous avez atteint
un mur dans votre recherche, vous revenez au dernier point connu où
vous avez pris une décision avant le mur, et choisissez
un chemin différent.

Tests.

    >>> csp.consistent(1, {1: 2})
    True

    >>> csp.consistent(1, {1: 2, 2: 4})
    True

    >>> csp.consistent(1, {1: 2, 2: 4, 3: 1})
    True

    >>> csp.consistent(1, {1: 2, 2: 4, 3: 1, 4: 1})
    True

    >>> csp.consistent(1, {1: 2, 2: 4, 3: 1, 4: 2})
    True

    >>> csp.consistent(1, {1: 2, 2: 4, 3: 1, 4: 3})
    True

    >>> csp.consistent(1, {1: 3})
    True

    >>> csp.consistent(1, {1: 3, 2: 1})
    True

    >>> csp.consistent(1, {1: 3, 2: 1, 3: 4})
    True

    >>> csp.consistent(1, {1: 3, 2: 1, 3: 4, 4: 2})
    True

## Classe `CSP`, `backtracking_search()`

Créer une instance.

     >>> csp = script.CSP([1, 2, 3, 4],{1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]})

Tests.
  
    >>> csp.backtracking_search({1: 2, 2: 4, 3: 1, 4: 1})
    assigné, {col: ran}, {1: 2, 2: 4, 3: 1, 4: 1}; {1: 2, 2: 4, 3: 1, 4: 1}
