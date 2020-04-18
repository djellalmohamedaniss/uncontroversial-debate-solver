class Vote:
    
    def __init__(self, attack, expert, polarity=0):
        self.attack = attack
        self.expert = expert
        self.polarity = polarity
        
    def __repr__(self):
        return "expert {0} votes {1} on {2}".format(self.expert.name,self.polarity,str(self.attack))
