from Globals import liste_arc, liste_topic


class Attack:

    def __init__(self, first_argument, second_argument):
        if ((first_argument.name, second_argument.name) in liste_arc):
            self.first_argument = first_argument
            self.second_argument = second_argument
            self.ev = [0,0]
        else:
            raise Exception("the attack ({0},{1}) does not exist".format(
                first_argument.name, second_argument.name))
            
    def __repr__(self):
        return "({0},{1},<{2},{3}>)".format(str(self.first_argument),str(self.second_argument),self.ev[0],self.ev[1])

    
    def __eq__(self,obj):
        return self.first_argument.name == obj.first_argument.name and self.second_argument.name == obj.second_argument.name
    
    def top(self):
        return self.first_argument.top() + self.second_argument.top()
    
    def edit_weight(self,new):
        u=list(self.ev)
        u[0]= new
        self.ev = tuple(u)
    
    def apply_votes(self,votes):
        self.votes = votes
        self.ev = self.evaluation_vector()

    def prominent(self):
        prom = []
        for t in liste_topic:
            if (t in self.first_argument.top() and t in self.second_argument.top()):
                prom.append(t)
        return prom

    def relevant(self):
        liste_rel = []
        for t in liste_topic:
            if(t in self.first_argument.top() and t not in self.second_argument.top()):
                liste_rel.append(t)
            elif(t not in self.first_argument.top() and t in self.second_argument.top()):
                liste_rel.append(t)
        return liste_rel

    def irrelevant(self):
        non_pert = []
        for t in liste_topic:
            if (t not in self.first_argument.top() and t not in self.second_argument.top()):
                non_pert.append(t)
        return non_pert

    def evaluation_vector(self):
        eva_vector = [0, 0]
        for vote in self.votes:
            if self != vote.attack or vote.expert.impact(self) == 0:
                continue
            else:
                eva_vector[0] = eva_vector[0] + \
                    vote.polarity * vote.expert.impact(self)
                eva_vector[1] = eva_vector[1] + len(self.top())
        return tuple(eva_vector)
    
    def is_beyond_any_doubt(self):
        return not self.is_strong() and not self.is_weak()
        
        
    def is_strong(self):
        ev_vector = self.evaluation_vector()
        return ( ev_vector[0] > 0 and ( ev_vector[0] - len(self.top()) )  > 0 ) or ( ev_vector[0] <= 0 and ( abs(ev_vector[0]) - len(self.top()) )  >= 0)
    
    def is_weak(self):
        ev_vector = self.evaluation_vector()
        return ( ev_vector[0] > 0 and ( ev_vector[0] - len(self.top()) )  <= 0 ) or ( ev_vector[0] <= 0 and ( abs(ev_vector[0]) - len(self.top()) )  < 0 )

        
        
        
    
    
