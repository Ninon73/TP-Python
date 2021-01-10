from exceptions import SommetInexistantException, SommetExisteDejaException

class Sommets():
    def __init__(self, set_sommet=None):
        if set_sommet is None:
            set_sommet = set()
        self._check_set_sommet(set_sommet)
        self.V = set_sommet

    @staticmethod
    def _check_set_sommet(set_sommet):
        if not isinstance(set_sommet, set):
            raise TypeError("La classe Sommet doit être instantiée avec un set de Sommet")
        for sommet in set_sommet:
            if not isinstance(sommet, Sommet):
                raise TypeError("L'un des éléments du set pour instantier un objet de la classe Sommets n'est pas de classe Sommet")

    def get(self, name):
        for v in self.V:
            if v.name == name:
                return v
        raise SommetInexistantException("Le sommet {} ne se trouve pas dans la liste".format(name))

    def add(self, sommet):
        for v in self.V:
            if v==sommet:
                raise SommetExisteDejaException("Le sommet existe déjà")
        self.V.add(sommet)

    def __str__(self):
        rtn = "L'ensemble de Sommet V est: \n{"
        for v in self.V:
            rtn+=v.__str__()
            rtn+=", "
        rtn = rtn[:-2] if len(self.V)>0 else rtn
        rtn+="}"
        return rtn


class Sommet():
    def __init__(self, name):
        self.name = name

    def __eq__(self, s):
        return self.name == s.name

    def __hash__(self):
        return hash(self.name)

    @classmethod
    def instantiate_sommet(cls):
        nom_sommet = input("Nom du sommet: ")
        return Sommet(nom_sommet)

    def __str__(self):
        return self.name
