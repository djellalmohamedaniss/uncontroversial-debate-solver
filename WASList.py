from itertools import permutations
from PossibleWAS import PossibleWASList as PossibleWAS
from prettytable import PrettyTable
from termcolor import colored


class WASList:
    def __init__(self,was_dict):
        self.was_dict = was_dict
        
    def find_was_of_expert(self,expert):
        expert_list = expert.split(',')
        topics_combinations = [",".join(comb) for comb in permutations(expert_list,len(expert_list))]
        for combination in topics_combinations:
            if combination in self.was_dict:
                return self.was_dict[combination]
        raise Exception("the expert {0} does not exist".format(expert))
        
    
    def reinforcers(self):
        experts = list(self.was_dict.keys())
        for expert1 in experts:
            for expert2 in experts:
                if expert1 != expert2:
                    if PossibleWAS.is_reinforce_dominate(self.was_dict[expert1],self.was_dict[expert2]):
                        print("{0} necessarily reinforce-dominates {1}".format(expert1,expert2))
                        
    
    # prettyTable for possible was print
    def table_possible_was(self):
        x = PrettyTable()
        first_element_key = list(self.was_dict.keys())[0]
        first_element = self.was_dict[first_element_key]
        l=["expert"]
        for e in first_element:
            l.append("({0}),s={1}".format(e['attack'],e['polarity']))
        x.field_names = l
        for expert,expert_effect in self.was_dict.items():
            l=[expert]
            for ee in expert_effect:
                if ee['was'].liste_arc_dict[ee['attack']].is_strong():
                    p = colored(str(ee['was'].liste_arc_dict[ee['attack']].ev),color="white",on_color='on_red')
                    l.append(p)
                else:
                    l.append(ee['was'].liste_arc_dict[ee['attack']].ev)
            x.add_row(l)
            x.align["expert"] = "l"
        return x