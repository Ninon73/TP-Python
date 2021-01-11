from sommet import Sommet, get_sommet
from arc import Arc
import copy


class Graphe():
    def __init__(self, V, E):
        self.V = V
        self.E = E

    def get_liste_arc_init(self, v):
        rtn = []
        for e in self.E:
            if v == e.e[0]:
                rtn.append(e)
        return rtn

    def get_liste_arc_final(self, v):
        rtn = []
        for e in self.E:
            if v == e.e[1]:
                rtn.append(e)
        return rtn

    def get_sommet(self, nom_sommet):
        return get_sommet(self.V, nom_sommet)

    def degre_interieur(self, nom_sommet):
        v = self.get_sommet(nom_sommet)
        n = len(self.get_liste_arc_init(v))
        return n

    def degre_exterieur(self, nom_sommet):
        v = self.get_sommet(nom_sommet)
        n = len(self.get_liste_arc_final(v))
        return n

    def degre(self, nom_sommet):
        return self.degre_interieur(nom_sommet) + self.degre_exterieur(nom_sommet)

    def plusCourtChemin(self, sommet1, sommet2):
        # TODO
        s1 = self.get_sommet(sommet1)
        s2 = self.get_sommet(sommet2)
        all_chemins = self._listeChemin(s1, s2, set())
        map_arc_val = {i: sum((arc.val for arc in arcs)) for i, arcs in enumerate(all_chemins)}
        rtn = min({v[1] for v in map_arc_val.items()})
        id_chemin_res = [i[0] for i in map_arc_val.items() if i[1] == rtn]
        chemin_res = [v for i,v in enumerate(all_chemins) if i in id_chemin_res]
        return rtn, chemin_res

    def _listeChemin(self, sommet1, sommet2, arcs):
        if sommet1 == sommet2:
            return arcs

        init_arcs = set(self.get_liste_arc_init(sommet1))
        init_arcs_non_explore = init_arcs - arcs
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
        V = {}
        for i in range(nb_sommet):
            print("{}:".format(i + 1))
            s = Sommet.instantiate_sommet()
            V.add(s)

        nb_arc = int(input("Combien y a t-il d'arc ?"))
        E = {}
        for i in range(nb_arc):
            print("{}:".format(i + 1))
            arc_cur = Arc.instantiate_arc(V)
            E.add(arc_cur)

        g = Graphe(V, E)
        return g

    @classmethod
    def instantiate_graph_from_file(cls, file_path):
        V = set()
        E = set()

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
                    arc = Arc(get_sommet(V, si), get_sommet(V, sf), float(val))
                    E.add(arc)

        g = Graphe(V, E)
        return g

    def __str__(self):
        rtn = "-" * 80
        rtn += "\nLa représentation du graphe est:\n"
        rtn += "{"
        for v in self.V:
            rtn += v.__str__()
        rtn += "}\n"
        for e in self.E:
            rtn += e.__str__()
        rtn += "-" * 80
        rtn += "\n"
        return rtn
