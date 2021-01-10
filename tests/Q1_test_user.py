#Q1:
# On défini la class Sommet qui est en réalité juste un nom
# On défini la class Sommets qui est un ensemble de sommet, on s'assure qu'on ne puisse pas créer deux fois le même sommet.
# On crée une méthode pour qu'un utilisateur puisse instantier un Sommet.
# On défini la class Arc qui est composé de deux sommets (initial et final qu'on représente avec un tupple), et d'une valeur.
# On défini la class Arcs qui est un ensemble d'arc.

# On crée les méthodes pour ajouter des elts Arc à la classe Arcs et des éléments Sommet à la classe Sommet
# On crée une méthode pour qu'un utilisateur puisse instantier un arc lorsqu'on a déjà l'objet Sommets (i.e. la liste de sommets)
# Cela permet donc d'ajouter les éléments Sommet qu'on a déjà instantier plutôt que de réinstantier de nouveaux objets sommet.

# On crée la class graphe qui est composé d'un ensemble de Sommet et un ensemble d'arcs, il y a donc un attribut de classe Sommets
# et un attribut de class Arcs
# On crée une méthode de classe qui permet à l'utilisateur de créer un graphe comme l'indique la Q1.

import sys
sys.path.append("../src/")
from graphe import Graphe
graph = Graphe.instantiate_graph_from_input()
print(graph)
