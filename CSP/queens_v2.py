from typing import Dict, List, Optional
import os
import sys
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from csp_v2 import Constraint, CSP

# Les modules numpy et pandas permettre de créer des matrices carrés
# pour représenter les échiquiers

# Le module seaborn (dérivé de matplotlib)
# comporte le graphique heatmap qui permet
# de transformer une matrice (numpy ou pandas)
# en un plan 3D où les colonnes (a à d) et les rangées (1 à 4) montrent
# des 0 ou des 1 (3e dimension) sous la forme de couleurs avec
# une échelle de couleur discrète de 0 à 1

# Le module datetime permet de créer un chronomètre pour
# mesurer le temps d'exécution
# La mesure n'est pas aussi précise qu'avec le module timeit,
# mais timeit prend beaucoup de temps en testant
# une exécution plusieurs fois afin calculer
# le temps moyen d'exécution et son écart-type

# queens.py
# From Classic Computer Science Problems in Python Chapter 3
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class QueensConstraint(Constraint[int, int]):
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
            # q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]  # q2r = queen 2 row
                    print(q1c, q1r, q2c, q2r)
                    if q1r == q2r:  # same row?
                        print("Orthogonal !!!")
                        print(self.dessiner_echiquier(q1c, q1r, q2c, q2r))
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):  # same diagonal?
                        print("Diagonale !!!")
                        print(self.dessiner_echiquier(q1c, q1r, q2c, q2r))
                        return False
                    print("--- OK ---")
                    print(self.dessiner_echiquier(q1c, q1r, q2c, q2r))
        return True  # no conflict

    def dessiner_echiquier(self,
                           col1: int, row1: int,
                           col2: int, row2: int) -> pd.DataFrame:
        """Dessiner la matrice de l'échiquier
        de chaque essais de l'algorithme de CSP dans le problème nQueens"""
        # Créer un ndarray
        echiquier_ndarray: np.array[str] = np.ones((len(self.columns),
                                                    len(self.columns)),
                                                   dtype=str)
        # Modifier le items du ndarray
        echiquier_ndarray[echiquier_ndarray == '1'] = "-"
        # Convertir le ndarray en DataFrame
        echiquier: pd.DataFrame[str] = \
            pd.DataFrame(echiquier_ndarray,
                         index=range(1, len(self.columns)+1, 1),
                         columns=range(1, len(self.columns)+1, 1))
        # Imputer 2 dames au DataFrame
        echiquier.loc[row1, col1]: pd.DataFrame[str] = 'Q'
        echiquier.loc[row2, col2]: pd.DataFrame[str] = 'Q'
        # Retourner le DataFrame
        return echiquier


class Final:
    """Visualiser la solution du problème nQueens
    avec une matrice et un graphique"""

    @classmethod
    def creer_echiquier_final(cls, new_solution: Dict[int, int],
                              tai: int) -> np.ndarray:
        """Dessiner la matrice de l'échiquier
        de la solution nQueens"""
        # Construire une clé de correspondance
        new_rows: Dict[int, str] = {1: "a", 2: "b", 3: "c",
                                    4: "d", 5: "e", 6: "f",
                                    7: "g", 8: "h"}
        # Convertir les rangées numériques
        # en rangées alphabétiques
        for cle, val in new_solution.items():
            new_solution[cle]: str = new_rows[val]
        # Créer un ndarray
        echiquier_ndarray2 = np.zeros((tai, tai), dtype=int)
        # Construire une liste de colonnes alphabétique
        echiquier_col: List[str] = ["a", "b", "c",
                                    "d", "e", "f",
                                    "g", "h"]
        # Déterminer la taille de la liste
        # de colonnes alphabétiques et
        # envoyer le résultat dans une liste
        echiquier_col: List[str] = echiquier_col[0:tai]
        # Convertir le ndarray en DataFrame
        # selon un index de lignes basé sur
        # le nombre de colonnes et
        # un index de colonnes basé sur
        # la liste précédente
        echiquier_fin = pd.DataFrame(echiquier_ndarray2,
                                     index=range(tai, 0, -1),
                                     columns=echiquier_col)
        # Changer des cases de l'échiquier avec
        # la solution; remplacer 0 par 1
        for cle, val in new_solution.items():
            echiquier_fin.loc[cle, val]: int = 1
        # Créer l'échiquier final
        # avec le DataFrame
        return echiquier_fin

    @classmethod
    def dessiner_echiquier_final(cls, echiquier_final):
        """Dessiner le graphique de l'échiquier
        de la solution nQueens"""
        sns.heatmap(echiquier_final,
                    linecolor="white",
                    cbar=False,
                    cmap='coolwarm',
                    linewidths=1,
                    square=True,
                    vmin=0,
                    vmax=1)
        plt.title("Échiquier final")

        # Sauvegarder le dessin
        plt.savefig('echiquier_final.png')


if __name__ == "__main__":
    # Démarrer le chrono
    depart = datetime.now()
    ####################
    # Interface
    ####################
    # Déterminer le répertoire de travail
    os.chdir(r"C:\Users\Usager\Documents\Ahuntsic\_420-316-AH INTELLIGENCE ARTIFICIELLE II\Projet")
    # DÉTERMINER la taille de l'échiquier de 4 à 10
    TAILLE: int = 5
    # DÉTERMINER l'algorithme
    # Backtracking Search  ou  Backtracking Search 2
    ALGORITHME = "BS"  # "BS2"
    """
    https://plcoster.github.io/homepage/blog-n-queens.html
    """
    ####################
    # Modélisation
    ####################
    print(f"Évaluer un échiquier de {TAILLE}x{TAILLE} \
avec l'algorithme {ALGORITHME}")
    # Déterminer les colonnes (lignes horizontales)
    cols: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10][0:TAILLE]
    print("colonnes,\n", cols)

    # Déterminer les rangées (lignes verticales)
    col_rows: Dict[int, List[int]] = {}
    for column in cols:
        col_rows[column] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10][0:TAILLE]
    print("k=colonnes, v=rangées, ")
    print("{colonnes: [rangées]},\n", col_rows)

    # Construire l'instance selon
    # taille de l'échiquier;
    # les variable, le domaine et la liste de contraintes
    csp: CSP[int, int] = CSP(cols, col_rows)
    print("variables,", csp.variables)
    print("domaine (colonne: rangée),", csp.domains)
    print("liste de contraintes,", csp.constraints)  # vide au départ

    # Ajouter les contraintes
    # nombre de Dames = nombre de colonnes
    csp.add_constraint(QueensConstraint(cols))
    for c in csp.constraints:
        print("contrainte de la liste,", c)

    ####################
    # Optimisation
    ####################
    print("ALGORITHME---------------------")
    # Valider et lancer l'algorithme
    if (TAILLE < 2) or (TAILLE > 10):
        print("Choisir une taille de 2 à 10 et relancer")
        sys.exit()
    try:
        if ALGORITHME == "BS":
            solution: Optional[Dict[int, int]] = csp.backtracking_search()
        elif ALGORITHME == "BS2":
            solution: Optional[Dict[int, int]] = csp.backtracking_search_2()
        else:
            print("Choisir un bon algorithme et relancer")
            sys.exit()
    except Exception:
        print("Choisir un bon algorithme et relancer")
        sys.exit()

    # Retourner la solution ou non
    if solution is None:
        print("No solution found!")
    else:
        print("\nSOLUTION---------------------")
        print("assigné, {col: ran},", solution)
        # Créer l'échiquier final
        echiquier_de_fin: np.ndarray = Final.creer_echiquier_final(solution, TAILLE)
        print("échiquier final,\n", echiquier_de_fin)
        # Dessiner l'échiquier final
        Final.dessiner_echiquier_final(echiquier_de_fin)
        print("CHRONO---------------------")
        # Arrêter le chrono
        arrivee = datetime.now()
        # Mesurer le temps
        temps = arrivee - depart
        secondes = temps.seconds + temps.microseconds / 1000000
        minutes = round((temps.seconds + temps.microseconds / 1000000) / 60, 2)
        print("Avec un datetime.timedelta sur"
              "2 datetime.datetime.now() (départ et arrivée),")
        print(f"un temps de {secondes}s")
        print(f"   ou environ {minutes}min")
