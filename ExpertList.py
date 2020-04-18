from itertools import permutations



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
        
        
    def find_by_expertise(self,expert_name):
        expert_list = expert_name.split(',')
        topics_combinations = [",".join(comb) for comb in permutations(expert_list,len(expert_list))]
        for expert in self.expert_list:
            for combination in topics_combinations:
                if ",".join(expert.expertise) == combination:
                    return expert
        raise Exception("the expert {0} does not exist".format(expert_name))