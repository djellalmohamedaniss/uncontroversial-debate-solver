from itertools import permutations
from networkx import networkx as nx



class ExpertList:
    
    def __init__(self,expert_list):
        self.expert_list = expert_list
        
    def __repr__(self):
        return str(self.expert_list)
    
    def __iter__(self):
        return iter(self.expert_list)

    def __next__(self):
        self.current += 1
        if self.current < len(self.expert_list):
            return self.current
        raise StopIteration
        
        
    def best(self):
        d=nx.DiGraph()
        d.add_nodes_from([expert.name for expert in self.expert_list])
        for exp in self.expert_list:
            for expert in self.expert_list:
                if exp.reinforce_dominate(expert):
                    d.add_edge(exp.name,expert.name)
        return [self.find_by_name(elem[0]) for elem in d.out_degree if max(d.out_degree, key=lambda x: x[1])[1] == elem[1]]
    
    
    def find_by_name(self,name):
        for expert in self.expert_list:
            if expert.name == name:
                return expert
        raise Exception("the expert {0} does not exist".format(name))
        
        
        
    def find_by_expertise(self,expert_name):
        expert_list = expert_name.split(',')
        topics_combinations = [",".join(comb) for comb in permutations(expert_list,len(expert_list))]
        for expert in self.expert_list:
            for combination in topics_combinations:
                if ",".join(expert.expertise) == combination:
                    return expert
        raise Exception("the expert {0} does not exist".format(expert_name))