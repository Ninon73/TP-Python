# Q2:
# On rajoute une méthode de classe qui permet à l'utilisateur de créer le graphe directement
# depuis un fichier via. instantiate_graph_from_file
import sys

sys.path.append("../src/")
from graphe import Graphe

graph = Graphe.instantiate_graph_from_file("test_degree.txt")

size, res = graph.plusCourtChemin("A", "F")
print(size, "Nb chemin min: {}".format(len(res)))
for i in res:
    print(i)

deg = graph.degre("A")
print("Degré de A est: {}".format(deg))
