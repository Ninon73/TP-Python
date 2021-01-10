from sommet import Sommet, Sommets
from arc import Arc, Arcs
from exceptions import ArcInexistantException

class Graphe():
    def __init__(self, V=None, E=None):
        if V is None:
            V = {}
        if E is None:
            E = {}
        self._check_V(V)
        self._check_E(E, V)
        self.V = V
        self.E = E

    @staticmethod
    def _check_V(V):
        if not (isinstance(V, Sommets)):
            raise TypeError("L'ensemble V doit être de classe Sommets")

    @staticmethod
    def _check_E(E, V):
        if not (isinstance(E, Arcs)):
            raise TypeError("L'ensemble E doit être de classe Arcs")

        for e in E.E:
            if not (e.e[0] in V.V):
                raise InvalideArcException("L'arc initial n'est pas dans l'ensemble de sommet")

            if not (e.e[1] in V.V):
                raise InvalideArcException("L'arc final n'est pas dans l'ensemble de sommet")

    @classmethod
    def instantiate_graph_from_input(cls):
        nb_sommet = int(input("Combien y a t-il de sommet ?"))
        V = Sommets()
        for i in range(nb_sommet):
            print("{}:".format(i+1))
            s = Sommet.instantiate_sommet()
            V.add(s)

        nb_arc = int(input("Combien y a t-il d'arc ?"))
        E = Arcs()
        for i in range(nb_arc):
            print("{}:".format(i+1))
            arc_cur = Arc.instantiate_arc(V)
            E.add(arc_cur)

        g = Graphe(V, E)
        return g

    @classmethod
    def instantiate_graph_from_file(cls, file_path):
        V = Sommets()
        E = Arcs()

        with open(file_path) as fp:
            line = fp.readline().rstrip('\n')
            if (line[0]!="{") or (line[-1]!="}"):
                raise Exception("Mauvais format")
            sommets = line[1:-1].replace(" ","").split(",")

            for i in sommets:
                V.add(Sommet(i))

            while line:
                line = fp.readline().rstrip('\n')
                if line:
                    si, sf, val = line.split("-")
                    arc = Arc(V.get(si), V.get(sf), float(val))
                    E.add(arc)

        g = Graphe(V,E)
        return g

    def __str__(self):
        rtn = "-"*80
        rtn+="\nLa représentation du graphe est:\n"
        rtn+=self.V.__str__()
        rtn+="\n"
        rtn+=self.E.__str__()
        rtn+="-"*80
        rtn+="\n"
        return rtn
