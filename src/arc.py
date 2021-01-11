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
