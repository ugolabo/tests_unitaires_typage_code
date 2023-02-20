from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

# csp.py
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

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type

# Base class for all constraints
# Classe abstraite
class Constraint(Generic[V, D], ABC):
    """Gabarit pour créer les contraintes du CSP"""

    # The variables that the constraint is between
    # Constructeur abstrait comme modèle
    def __init__(self, variables: List[V]) -> None:
        """Gabarit du constructeur pour les contraintes du CSP"""
        # Le modèle oblige l'emploi de cet attribut
        self.variables = variables

    # Must be overridden by subclasses
    # Méthode abstrainte comme modèle
    # qui oblige l'emploi de cette méthode
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        """Gabarit de méthode pour valider les contraintes du CSP"""
        ...


# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    """Appliquer un algorithme de CSP à un problème"""

    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        """"Construire une instance de problème
        avec des variables et un domaine pour les variables"""
        self.variables: List[V] = variables  # variables to be constrained
        self.domains: Dict[V, List[D]] = domains  # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        # Valider que chaque variable est dans le domaine
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should \
have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        """"Ajouter les contraintes du problèmes"""
        # Selon la liste vide construite dans la validation dans __init__
        for variable in constraint.variables:
            # Valider une 2e fois
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            # Ajouter (si la validation est bonne)
            # la contrainte dans la liste construire dans __init__
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        """"Valider si les variables assignées demeurent
        dans le domaine des variables selon les contraintes"""
        for constraint in self.constraints[variable]:
            print("constraint,", constraint,
                  "; variable (col),", variable,
                  "; assigné, {col: ran}", assignment)
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self,
                            assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        """"Appliquer un algorithme au problème; déterminer
        les variables non assignées et
        choisir la 1re des variables non assignées
        selon l'ordre statique"""
        # assignment is complete if every variable is assigned (our base case)
        print("assigné, {col: ran},", assignment, end="; ")
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        print("NON assigné, [col]", unassigned)

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]

        for value in self.domains[first]:
            print("valeur du domaine (ran),", value)
            local_assignment = assignment.copy()
            local_assignment[first] = value
            print("assigné local, {col: ran},", local_assignment)
            # if we're still consistent, we recurse (continue)
            print("consistent,", self.consistent(first, local_assignment))
            if self.consistent(first, local_assignment):  # if True
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None

    def backtracking_search_2(self,
                              assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        """"Appliquer un algorithme au problème; déterminer
        les variables non assignées et
        choisir la 2e des variables non assignées
        selon l'ordre statique"""
        # assignment is complete if every variable is assigned (our base case)
        print("assigné, {col: ran},", assignment, end="; ")
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        print("non assigné, [col]", unassigned)

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[1]

        for value in self.domains[first]:
            print("valeur du domaine (ran),", value)
            local_assignment = assignment.copy()
            local_assignment[first] = value
            print("assigné local, {col: ran},", local_assignment)
            # if we're still consistent, we recurse (continue)
            print("consistent,", self.consistent(first, local_assignment))
            if self.consistent(first, local_assignment):  # if True
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None
