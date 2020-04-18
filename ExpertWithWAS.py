from Expert import Expert
from itertools import combinations

class ExpertWithWAS(Expert):
    
    def __init__(self,name, arguments, expertise):
        super().__init__(name,arguments,expertise)
        
            
    def __repr__(self):
        return "potential expert <{0}> with expertise in {1}".format(self.name, self.expertise, self.arguments)
        
    def set_possible_was(self,possible_was):
        self.possible_was = possible_was
        
    def get_possible_was(self):
        return self.possible_was
    
    def get_was_maximum_stable_attack(self):
        return self.possible_was.get_was_maximum_stable_attack()
    
    def get_was_maximum_unstable_attack(self):
        return self.possible_was.get_was_maximum_unstable_attack()
    
    def necessarily_dominate(self,expert):
        was1 = self.get_was_maximum_unstable_attack()
        was2 = expert.get_was_maximum_stable_attack()
        return all(elem in was1.stable_attacks() for elem in was2.stable_attacks())

    def reinforce_dominate(self,expert):
        return self.optimisticaly_reinforce_dominate(expert) and self.pessimisticaly_reinforce_dominate(expert)
    
    
    def pessimisticaly_reinforce_dominate(self,expert):
        was1 = self.get_was_maximum_unstable_attack()
        was2 = expert.get_was_maximum_unstable_attack()
        return all(elem in was2.unstable_attacks()  for elem in was1.unstable_attacks())
    
    def optimisticaly_reinforce_dominate(self,expert):
        was1 = self.get_was_maximum_stable_attack()
        was2 = expert.get_was_maximum_stable_attack()
        return all(elem in was1.stable_attacks() for elem in was2.stable_attacks())
    
    @staticmethod
    def __generator__(topics,expertise_cardinal):
        experts = []
        combins = [list(comb) for comb in combinations(topics, expertise_cardinal)]
        i = 1
        for combin in combins:
            expert = ExpertWithWAS("EX{0}".format(i),[],combin)
            experts.append(expert)
            i=i+1
        return experts
        