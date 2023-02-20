# Tester le module queens.py

    >>> import queens_v2 as script
   
## Classe `QueensConstraint`, constructeur `__init__()`

Créer des instances.

    >>> queens4 = script.QueensConstraint(columns=[1 ,2, 3, 4])
    >>> queens5 = script.QueensConstraint(columns=[1, 2, 3, 4, 5])
    
Tests.

    >>> queens4.variables
    [1, 2, 3, 4]
    
    >>> queens4.columns
    [1, 2, 3, 4]

    >>> queens5.variables
    [1, 2, 3, 4, 5]
    
    >>> queens5.columns
    [1, 2, 3, 4, 5]

## Classe `QueensConstraint`, méthode `satisfied()`

Créer une instance.

    >>> queens = script.QueensConstraint(columns=[1 ,2, 3, 4])

Tests.

    >>> queens.satisfied(assignment={1: 1})
    True

    >>> queens.satisfied(assignment={1: 1, 2: 1})
    1 1 2 1
    Orthogonal !!!
       1  2  3  4
    1  Q  Q  -  -
    2  -  -  -  -
    3  -  -  -  -
    4  -  -  -  -
    False

    >>> queens.satisfied(assignment={1: 1, 2: 2})
    1 1 2 2
    Diagonale !!!
       1  2  3  4
    1  Q  -  -  -
    2  -  Q  -  -
    3  -  -  -  -
    4  -  -  -  -
    False

    >>> queens.satisfied(assignment={1: 1, 2: 3})
    1 1 2 3
    --- OK ---
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  Q  -  -
    4  -  -  -  -
    True

    >>> queens.satisfied(assignment={1: 1, 2: 3, 3: 1})
    1 1 2 3
    --- OK ---
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  Q  -  -
    4  -  -  -  -
    1 1 3 1
    Orthogonal !!!
       1  2  3  4
    1  Q  -  Q  -
    2  -  -  -  -
    3  -  -  -  -
    4  -  -  -  -
    False
 
    >>> queens.satisfied(assignment={1: 1, 2: 3, 3: 2})
    1 1 2 3
    --- OK ---
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  Q  -  -
    4  -  -  -  -
    1 1 3 2
    --- OK ---
       1  2  3  4
    1  Q  -  -  -
    2  -  -  Q  -
    3  -  -  -  -
    4  -  -  -  -
    2 3 3 2
    Diagonale !!!
       1  2  3  4
    1  -  -  -  -
    2  -  -  Q  -
    3  -  Q  -  -
    4  -  -  -  -
    False

    >>> queens.satisfied(assignment={1: 1, 2: 3, 3: 3})
    1 1 2 3
    --- OK ---
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  Q  -  -
    4  -  -  -  -
    1 1 3 3
    Diagonale !!!
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  -  Q  -
    4  -  -  -  -
    False

    >>> queens.satisfied(assignment={1: 1, 2: 3, 3: 4})
    1 1 2 3
    --- OK ---
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  Q  -  -
    4  -  -  -  -
    1 1 3 4
    --- OK ---
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  -  -  -
    4  -  -  Q  -
    2 3 3 4
    Diagonale !!!
       1  2  3  4
    1  -  -  -  -
    2  -  -  -  -
    3  -  Q  -  -
    4  -  -  Q  -
    False

## Classe `QueensConstraint`, méthode `dessiner_echiquier()`

Créer une instance.

    >>> queens = script.QueensConstraint(columns=[1, 2, 3, 4])

Tests.

    >>> queens.dessiner_echiquier(1,1,2,1)
       1  2  3  4
    1  Q  Q  -  -
    2  -  -  -  -
    3  -  -  -  -
    4  -  -  -  -

    >>> queens.dessiner_echiquier(1,1,2,2)
       1  2  3  4
    1  Q  -  -  -
    2  -  Q  -  -
    3  -  -  -  -
    4  -  -  -  -

    >>> queens.dessiner_echiquier(1,1,2,3)
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  Q  -  -
    4  -  -  -  -

    >>> queens.dessiner_echiquier(1,1,2,4)
       1  2  3  4
    1  Q  -  -  -
    2  -  -  -  -
    3  -  -  -  -
    4  -  Q  -  -
   
## Classe `Final`, méthode `creer_echiquier_final()`

Tests.

    >>> sols = {1: 2, 2: 4, 3: 1, 4: 3}
    >>> taille = 4
    >>> script.Final.creer_echiquier_final(new_solution=sols, tai=taille)
       a  b  c  d
    4  0  0  1  0
    3  1  0  0  0
    2  0  0  0  1
    1  0  1  0  0

    >>> sols = {1: 3, 2: 1, 3: 4, 4: 2}
    >>> taille = 4
    >>> script.Final.creer_echiquier_final(new_solution=sols, tai=taille)
       a  b  c  d
    4  0  1  0  0
    3  0  0  0  1
    2  1  0  0  0
    1  0  0  1  0