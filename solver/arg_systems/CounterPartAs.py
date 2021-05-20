from solver.core.AS import AS
import networkx as nx

class CounterPartAs(AS):
    
    
    def __init__(self,WAS):
        self.liste_noeud = WAS.liste_noeud
        self.__generate_counter_part_nx__(self,WAS)
        
        
        
    @staticmethod
    def __generate_counter_part_nx__(self,WAS):
        # clear graph
        CG=nx.DiGraph()
        CG = WAS.get_DG().to_directed()
        [CG.remove_edge(*(u,v)) for (u,v,d) in WAS.get_DG().edges(data=True) if d['weight'] <= 0]
        self.DG = CG
        la = []
        for attack in WAS.liste_arc:
            if attack.ev[0] > 0:
                la.append(attack)
        self.liste_arc = la
        
    
    def get_arguments_labeled_with_IN(self):
        l_in=list.copy(self.liste_noeud)
        for argument in self.liste_noeud:
            for attack in self.liste_arc:
                if argument == attack.second_argument and argument in l_in:
                    l_in.remove(argument)
        return l_in

    
    def get_arguments_labeled_with_OUT(self):
        l_out=[]
        l_in=self.get_arguments_labeled_with_IN()
        for argument in self.liste_noeud:
            if  any(item in self.get_attackers(argument) for item in l_in):
                l_out.append(argument)
        return l_out
    
    def get_arguments_labeled_with_UND(self):
        l = [item for item in self.liste_noeud if item not in self.get_arguments_labeled_with_OUT()]
        return [item for item in l if item not in self.get_arguments_labeled_with_IN()]
        
    
    
        
    
            
                
            
    