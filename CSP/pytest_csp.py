import csp_v2 as script
from queens_v2 import QueensConstraint
from typing import List, Dict

# Dans une console cmd
# au niveau du dossier où ce trouve ce fichier pytest,
# lancer la commande pytest
# Constater les résultats dans la console cmd

# La classe TestConstraint() est crée pour tester
# et il est un constraint


class TestConstraint(script.Constraint[int, int]):
    """Appliquer des contraintes de CSP
    à un problème nQueens"""

    def __init__(self, columns: List[int]) -> None:
        """Constructeur pour les contraintes du CSP appliquées à nQueens"""
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        """Valider les contraintes du CSP appliquées
        à un problème nQueens"""
        # Lancer la séquence d'essais
        # q1c = queen 1 column, q1r = queen 1 row
        # 1,1 est en haut à gauche et on place c:r
        # (c équivaut à variables, r équivaut à domains)
        # mais 1,1 sur l'échiquier est 1,4 ou a,4
        for q1c, q1r in assignment.items():
            if q1c == 1:
                if q1r == 3:
                    return False
        return True  # no conflict


# Classe CSP, constructeur __init__()

# Créer un mock
csp = script.CSP([1, 2, 3, 4],
                 {1: [1, 2, 3, 4],
                  2: [1, 2, 3, 4],
                  3: [1, 2, 3, 4],
                  4: [1, 2, 3, 4]})

csp2 = script.CSP([1, 2, 3, 4, 5],
                  {1: [1, 2, 3, 4, 5],
                   2: [1, 2, 3, 4, 5],
                   3: [1, 2, 3, 4, 5],
                   4: [1, 2, 3, 4, 5],
                   5: [1, 2, 3, 4, 5]})


# Tests
def test_csp_4_variables():
    assert csp.variables == [1, 2, 3, 4]


def test_csp_5_variables():
    assert csp2.variables == [1, 2, 3, 4, 5]


def test_csp_4_domains():
    assert csp.domains == {1: [1, 2, 3, 4],
                           2: [1, 2, 3, 4],
                           3: [1, 2, 3, 4],
                           4: [1, 2, 3, 4]}


def test_csp_5_domains():
    assert csp2.domains == {1: [1, 2, 3, 4, 5],
                            2: [1, 2, 3, 4, 5],
                            3: [1, 2, 3, 4, 5],
                            4: [1, 2, 3, 4, 5],
                            5: [1, 2, 3, 4, 5]}


def test_csp_4_constraints():
    assert csp.constraints == {1: [], 2: [], 3: [], 4: []}


def test_csp_5_constraints():
    assert csp2.constraints == {1: [], 2: [], 3: [], 4: [], 5: []}


# Classe CSP, méthode add_constraint()

# Créer un mock
# csp = script.CSP([1, 2, 3, 4],
# csp = script.CSP([1, 2, 3, 4],
#                  {1: [1, 2, 3, 4],
#                   2: [1, 2, 3, 4],
#                   3: [1, 2, 3, 4],
#                   4: [1, 2, 3, 4]})



# Tests
def test_add_constraint1():
    cols: List[int] = [1, 2, 3, 4]
    ssff = QueensConstraint(cols)
    print("ssff", ssff)
    csp.add_constraint(ssff)

    assert len(csp.constraints[1]) == 1
    assert len(csp.constraints[2]) == 1
    assert len(csp.constraints[3]) == 1

    ssss = TestConstraint([1])
    csp.add_constraint(ssss)

    assert len(csp.constraints[1]) == 2
    assert len(csp.constraints[2]) == 1
    assert len(csp.constraints[3]) == 1

    assert csp.constraints[1][0] == ssff
    assert csp.constraints[1][1] == ssss

    assert csp.constraints[2][0] == ssff


# Classe CSP, méthode consistent()

# Créer un mock
# csp = script.CSP([1, 2, 3, 4],
# csp = script.CSP([1, 2, 3, 4],
#                  {1: [1, 2, 3, 4],
#                   2: [1, 2, 3, 4],
#                   3: [1, 2, 3, 4],
#                   4: [1, 2, 3, 4]})


# Tests
    def test_consistent():
        cols: List[int] = [1, 2, 3, 4]
        csp.add_constraint(QueensConstraint(cols))
        
        assert csp.consistent(1, {1: 3, 2: 1, 3: 4, 4: 2})
        assert csp.consistent(1, {1: 3, 2: 3, 3: 4, 4: 2}) == False

        csp.add_constraint(TestConstraint([1, 2]))
        
        assert csp.consistent(1, {1: 3, 2: 1, 3: 4, 4: 2}) == False
        assert csp.consistent(2, {1: 1, 2: 3, 3: 4, 4: 2}) == False

        assert csp.consistent(3, {1: 3, 2: 1, 3: 4, 4: 2})


# Classe CSP, backtracking_search()

# Créer un mock
# csp = script.CSP([1, 2, 3, 4],
#                  {1: [1, 2, 3, 4],
#                   2: [1, 2, 3, 4],
#                   3: [1, 2, 3, 4],
#                   4: [1, 2, 3, 4]})

# Tests
def test_backtracking_search():
    assert csp.consistent(1, {1: 2, 2: 2, 3: 1, 4: 3}) == False
    assert csp.consistent(1, {1: 2, 2: 4, 3: 1, 4: 3}) == True
    assert csp2.consistent(1, {1: 1, 2: 3, 3: 5, 4: 2, 5: 4}) == True
