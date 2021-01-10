#Question1
l_sommets=[]
l_arcs=[]

nb_sommets = int(input("Il y a combien de sommets ? "))

class Sommet:
    for i in range(1,nb_sommets+1):
        print("Nom du sommet ",i," :  ")
        s = input()
Sommet()

nb_arcs=int(input("Il y a combien d'arcs ?"))
class Arc:
    for i in range(1,nb_arcs+1):
        print("Arc ",i," :  ")
        input("   L'extrémité initiale est le sommet : ")
        input("   L'extrémité finale est le sommet : ")
        input("   Sa valeur est : ")
Arc()

class Graph:
    l_sommets=[Sommet()]
    l_arcs=[Arc()]
Graph()
        
#Question2
def constructFromFile():
    f = open("/Users/nanou/Desktop/CNAM 1A/Python/graphe.txt","r")
    while True:
        s = f.readline()
        if (s != ""):
            print(s)
        else:
            break;
    return s
print(constructFromFile())
graphe = constructFromFile()

#Question3




#Question4
def plusCourtChemin (sommet 1, sommet 2): 

def all_paths(graph, start, goal):
       queue = [(start, [start])]
       while queue:
           (v, path) = queue.pop(0)
           for next in graph[v] - set(path):
               if next == goal:
                   yield path + [next]
               else:
                   queue.append((next, path + [next]))

min_path = min(all_paths(graph, start, goal),key=len)


#Question5
def plusCourtCheminAvecObstacle (sommet 1, sommet 2, sommet 3):
    


#Question6
L=[]
def comparaison(graphe1,graphe2):
        for i in range (len(graphe1)):
        for j in range (len(graphe2)):
            if graphe1[i] == graphe2[j]:
                L.append(graphe1[i])
    return L

print(comparaison(graphe1,graphe2))


