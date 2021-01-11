from exceptions import SommetInexistantException

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


def get_sommet(list_sommet, name):
    for v in list_sommet:
        if v.name == name:
            return v
    raise SommetInexistantException(name)
