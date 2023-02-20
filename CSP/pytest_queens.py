from typing import Dict, List
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
import queens_v2 as script

# Dans une console cmd
# au niveau du dossier où ce trouve ce fichier pytest,
# lancer la commande pytest
# Constater les résultats dans la console cmd


# Classe QueensConstraint, constructeur __init__()

# Créer une instance
queens4 = script.QueensConstraint(columns=[1, 2, 3, 4])
queens5 = script.QueensConstraint(columns=[1, 2, 3, 4, 5])


# Tests
def test_queens_4_variables():
    assert queens4.variables == [1, 2, 3, 4]


def test_queens_4_columns():
    assert queens4.columns == [1, 2, 3, 4]


def test_queens_5_variables():
    assert queens5.variables == [1, 2, 3, 4, 5]


def test_queens_5_columns():
    assert queens5.columns == [1, 2, 3, 4, 5]


# Classe QueensConstraint, méthode satisfied()

# Créer une instance
queens = script.QueensConstraint(columns=[1, 2, 3, 4])


# Tests
def test_1_1_satisfied():
    assert queens.satisfied(assignment={1: 1}) is True


def test_1_1_2_1_satisfied():
    assert queens.satisfied(assignment={1: 1, 2: 1}) is False


def test_1_1_2_2_satisfied():
    assert queens.satisfied(assignment={1: 1, 2: 2}) is False


def test_1_1_2_3_satisfied():
    assert queens.satisfied(assignment={1: 1, 2: 3}) is True


def test_1_1_2_1_3_1_satisfied():
    assert queens.satisfied(assignment={1: 1, 2: 3, 3: 1}) is False


def test_1_1_2_1_3_2_satisfied():
    assert queens.satisfied(assignment={1: 1, 2: 3, 3: 2}) is False


def test_1_1_2_1_3_3_satisfied():
    assert queens.satisfied(assignment={1: 1, 2: 3, 3: 3}) is False


def test_1_1_2_1_3_4_satisfied():
    assert queens.satisfied(assignment={1: 1, 2: 3, 3: 4}) is False


# Classe QueensConstraint, méthode dessiner_echiquier()

# Créer une instance
queens = script.QueensConstraint(columns=[1, 2, 3, 4])


# Tests
# Attention au DataFrame; la liste 1 du dictionnaire devient une colonne, etc.
def test_dessiner_echiquier_1_1_2_1():
    df1: pd.DataFrame = queens.dessiner_echiquier(1, 1, 2, 1)
    df2: pd.DataFrame = pd.DataFrame({1: ['Q', '-', '-', '-'],
                                      2: ['Q', '-', '-', '-'],
                                      3: ['-', '-', '-', '-'],
                                      4: ['-', '-', '-', '-']},
                                     index=[1, 2, 3, 4])
    assert_frame_equal(df1, df2)


def test_dessiner_echiquier_1_1_2_2():
    df1: pd.DataFrame = queens.dessiner_echiquier(1, 1, 2, 2)
    df2: pd.DataFrame = pd.DataFrame({1: ['Q', '-', '-', '-'],
                                      2: ['-', 'Q', '-', '-'],
                                      3: ['-', '-', '-', '-'],
                                      4: ['-', '-', '-', '-']},
                                     index=[1, 2, 3, 4])
    assert_frame_equal(df1, df2)


def test_dessiner_echiquier_1_1_2_3():
    df1: pd.DataFrame = queens.dessiner_echiquier(1, 1, 2, 3)
    df2: pd.DataFrame = pd.DataFrame({1: ['Q', '-', '-', '-'],
                                      2: ['-', '-', 'Q', '-'],
                                      3: ['-', '-', '-', '-'],
                                      4: ['-', '-', '-', '-']},
                                     index=[1, 2, 3, 4])
    assert_frame_equal(df1, df2)


def test_dessiner_echiquier_1_1_2_4():
    df1: pd.DataFrame = queens.dessiner_echiquier(1, 1, 2, 4)
    df2: pd.DataFrame = pd.DataFrame({1: ['Q', '-', '-', '-'],
                                      2: ['-', '-', '-', 'Q'],
                                      3: ['-', '-', '-', '-'],
                                      4: ['-', '-', '-', '-']},
                                     index=[1, 2, 3, 4])
    assert_frame_equal(df1, df2)


# Classe Final, méthode creer_echiquier_final()


# Tests
# Attention au DataFrame; la liste a du dictionnaire devient une colonne, etc.
def test_creer_echiquier_final1():
    df1: pd.DataFrame = script.Final.\
        creer_echiquier_final(new_solution={1: 2, 2: 4, 3: 1, 4: 3}, tai=4)
    df2: pd.DataFrame = pd.DataFrame({"a": [0, 1, 0, 0],
                                      "b": [0, 0, 0, 1],
                                      "c": [1, 0, 0, 0],
                                      "d": [0, 0, 1, 0]},
                                     index=[4, 3, 2, 1],
                                     dtype='int32')
    assert_frame_equal(df1, df2)


def test_creer_echiquier_final2():
    df1: pd.DataFrame = script.Final.\
        creer_echiquier_final(new_solution={1: 3, 2: 1, 3: 4, 4: 2}, tai=4)
    df2: pd.DataFrame = pd.DataFrame({"a": [0, 0, 1, 0],
                                      "b": [1, 0, 0, 0],
                                      "c": [0, 0, 0, 1],
                                      "d": [0, 1, 0, 0]},
                                     index=[4, 3, 2, 1],
                                     dtype='int32')
    assert_frame_equal(df1, df2)
