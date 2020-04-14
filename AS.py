import networkx as nx

class AS:

 # Derived class from networkx directed graphs, nodes cannot be sets

    # constructeur qui prend en parametre la liste de noeuds et la liste darcs et qui cree un Digraph de nx
    def __init__(self, liste_noeud, liste_arc):
        self.DG = nx.DiGraph()
        self.liste_noeud = liste_noeud
        self.liste_arc = liste_arc
        self.__generate_nx__()
        
    def __generate_nx__(self):
        self.DG.add_nodes_from(self.arguments_to_string_list(self.liste_noeud))
        self.DG.add_edges_from(self.attacks_to_tuple(self.liste_arc))


    # getter method

    def get_DG(self):
        return self.DG

    def get_DG_nodes(self):  # reverifier
        return list(self.DG.nodes())
    # recuperation

    def get_nbr_arg(liste_arc):
        return len(liste_arc)
    # ou

    def get_nbr_arg2(self):
        return self.DG.number_of_edges()
    
    @staticmethod
    def arguments_to_string_list(liste_noeud):
        return list(map(str,liste_noeud))
    
    @staticmethod
    def show_graph_nx(graph):
        pos = nx.random_layout(graph)
        nx.draw(graph,pos,edge_color='black',width=1,linewidths=2,\
node_size=500,alpha=1,labels={node:node for node in graph.nodes()})
    
    @staticmethod
    def attacks_to_tuple(liste_arc):
        l = []
        for arc in liste_arc:
            l.append((str(arc.first_argument),str(arc.second_argument)))
        return l
    
        
    def get_attackers(self,attacked):
        attackers=[]
        for attack in self.liste_arc:
            if attacked == attack.second_argument:
                attackers.append(attack.first_argument)
        return attackers
        
