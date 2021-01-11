from exceptions import ArcExisteDejaException


class Arcs():
    def __init__(self, set_arc=None):
        if set_arc is None:
            set_arc = set()
        self._check_set_arc(set_arc)
        self.E = set_arc

    @staticmethod
    def _check_set_arc(set_arc):
        if not isinstance(set_arc, set):
            raise TypeError("La classe arcs ne peut être instantiée que par un set d'arcs")
        for arc in set_arc:
            if not isinstance(arc, Arc):
                raise TypeError(
                    "L'un des éléments du set pour instantier un object de la classe Arcs n'est pas de classe Arc")

    def add(self, arc):
        for e in self.E:
            if e == arc:
                print(e, arc, e.__hash__(), arc.__hash__())
                raise ArcExisteDejaException("L'arc existe déjà")
        self.E.add(arc)

    @property
    def val(self):
        val = 0
        for e in self.E:
            val += e.val
        return val

    def __str__(self):
        rtn = "L'ensemble d'Arcs E est:\n"
        for e in self.E:
            rtn += e.__str__()
            rtn += "\n"
        return rtn


class Arc():
    def __init__(self, sommet_i, sommet_f, val):
        self.e = (sommet_i, sommet_f)
        self.val = val

    def __eq__(self, arc):
        return (self.e == arc.e) and (self.val == arc.val)

    def __hash__(self):
        return hash((self.e, self.val))

    @classmethod
    def instantiate_arc(cls, V):
        nom_sommet_i = input("Nom du sommet initial: ")
        si = V.get(nom_sommet_i)  # On récupère l'objet dans la liste de sommet pour créer l'arc
        nom_sommet_f = input("Nom du sommet final: ")
        sf = V.get(nom_sommet_f)
        val = input("Valeur arc: ")
        arc = Arc(si, sf, val)
        return arc

    def __str__(self):
        rtn = "{}-{}-{}".format(self.e[0], self.e[1], self.val)
        return rtn
