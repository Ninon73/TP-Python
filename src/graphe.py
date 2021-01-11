from sommet import Sommet, Sommets
from arc import Arc, Arcs
from exceptions import SommetInexistantException
import copy


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
                raise SommetInexistantException("Le sommet initial de l'arc n'est pas dans l'ensemble de sommet")

            if not (e.e[1] in V.V):
                raise SommetInexistantException("Le sommet final de l'arc n'est pas dans l'ensemble de sommet")

    def get_liste_arc_init(self, v):
        rtn = []
        for e in self.E.E:
            if v == e.e[0]:
                rtn.append(e)
        return rtn

    def get_liste_arc_final(self, v):
        rtn = []
        for e in self.E.E:
            if v == e.e[1]:
                rtn.append(e)
        return rtn

    def degre_interieur(self, nom_sommet):
        v = self.V.get(nom_sommet)
        n = len(self.get_liste_arc_init(v))
        return n

    def degre_exterieur(self, nom_sommet):
        v = self.V.get(nom_sommet)
        n = len(self.get_liste_arc_final(v))
        return n

    def degre(self, nom_sommet):
        return self.degre_interieur(nom_sommet) + self.degre_exterieur(nom_sommet)

    def plusCourtChemin(self, sommet1, sommet2):
        # TODO
        s1 = self.V.get(sommet1)
        s2 = self.V.get(sommet2)
        all_chemins = list(self._listeChemin(s1, s2, Arcs()))

        map_arc_val = {arc: arc.val for arc in all_chemins}
        rtn = min({v[1] for v in map_arc_val.items()})
        chemin_res = [i[0] for i in map_arc_val.items() if i[1] == rtn]
        return rtn, chemin_res

    def _listeChemin(self, sommet1, sommet2, arcs):

        if sommet1 == sommet2:
            return arcs

        init_arcs = set(self.get_liste_arc_init(sommet1))
        init_arcs_non_explore = init_arcs - arcs.E
        all_res = []
        for e in init_arcs_non_explore:
            arcs_cur = copy.deepcopy(arcs)
            arcs_cur.add(e)
            res = self._listeChemin(e.e[1], sommet2, arcs_cur)
            if res is not None:
                if isinstance(res, list):
                    all_res.extend(res)
                else:
                    all_res.append(res)
        return all_res

    @classmethod
    def instantiate_graph_from_input(cls):
        nb_sommet = int(input("Combien y a t-il de sommet ?"))
        V = Sommets()
        for i in range(nb_sommet):
            print("{}:".format(i + 1))
            s = Sommet.instantiate_sommet()
            V.add(s)

        nb_arc = int(input("Combien y a t-il d'arc ?"))
        E = Arcs()
        for i in range(nb_arc):
            print("{}:".format(i + 1))
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
            if (line[0] != "{") or (line[-1] != "}"):
                raise Exception("Mauvais format")
            sommets = line[1:-1].replace(" ", "").split(",")

            for i in sommets:
                V.add(Sommet(i))

            while line:
                line = fp.readline().rstrip('\n')
                if line:
                    si, sf, val = line.split("-")
                    arc = Arc(V.get(si), V.get(sf), float(val))
                    E.add(arc)

        g = Graphe(V, E)
        return g

    def __str__(self):
        rtn = "-" * 80
        rtn += "\nLa représentation du graphe est:\n"
        rtn += self.V.__str__()
        rtn += "\n"
        rtn += self.E.__str__()
        rtn += "-" * 80
        rtn += "\n"
        return rtn
