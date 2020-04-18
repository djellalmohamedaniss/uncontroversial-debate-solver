class PossibleWASList:
    
    def __init__(self,possible_was_list):
        self.possible_was_list = possible_was_list
            
    
    def __repr__(self):
        return str(self.possible_was_list)
    
    
    def __iter__(self):
        return iter(self.possible_was_list)

    def __next__(self):
        self.current += 1
        if self.current < len(self.possible_was_list):
            return self.current
        raise StopIteration
        
        
    def get_was_maximum_stable_attack(self):
        c_maximal_was = None
        for possible_was in self.possible_was_list:
            if c_maximal_was == None:
                c_maximal_was = possible_was['was']
            elif len(possible_was['was'].stable_attacks()) >= len(c_maximal_was.stable_attacks()):
                c_maximal_was = possible_was['was']
        return c_maximal_was
    

    def get_was_maximum_unstable_attack(self):
        c_maximal_was = None
        for possible_was in self.possible_was_list:
            if c_maximal_was == None:
                c_maximal_was = possible_was['was']
            elif len(possible_was['was'].unstable_attacks()) >= len(c_maximal_was.unstable_attacks()):
                c_maximal_was = possible_was['was']
        return c_maximal_was
    
    
    def get_was_maximum_persistent_argument(self):
        c_maximal_was = None
        for possible_was in self.possible_was_list:
            if c_maximal_was == None:
                c_maximal_was = possible_was['was']
            elif len(possible_was['was'].persistant_arguments()) >= len(c_maximal_was.persistant_arguments()):
                c_maximal_was = possible_was['was']
        return c_maximal_was
    
    def get_was_maximum_nonpersistent_argument(self):
        c_maximal_was = None
        for possible_was in self.possible_was_list:
            if c_maximal_was == None:
                c_maximal_was = possible_was['was']
            elif len(possible_was['was'].non_persistant_arguments()) >= len(c_maximal_was.non_persistant_arguments()):
                c_maximal_was = possible_was['was']
        return c_maximal_was
        
    
        
        

