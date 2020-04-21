from AS import AS
import networkx as nx
from copy import deepcopy
from CounterPartAs import CounterPartAs
from Vote import Vote
from WASList import WASList
from ExpertList import ExpertList
from PossibleWAS import PossibleWASList as PossibleWAS


class WAS(AS):
    # Derived class from networkx directed graphs, nodes cannot be sets
    def __init__(self,liste_noeud,liste_arc):
        self.weights = [attack.evaluation_vector() for attack in list(liste_arc.values())]
        super().__init__(liste_noeud,liste_arc)

    
    def update_weights(self):
        self.weights = [attack.evaluation_vector() for attack in self.liste_arc]
        
        
    def __copy__(self):
        return deepcopy(self)
        
    def __repr__(self):
        return "\nnodes: {0} | attacks : stable : {1} , unstable : {2}\n".format(str(self.liste_noeud),str(self.stable_attacks()),str(self.unstable_attacks()))
    
    def __generate_nx__(self):
        self.DG.add_nodes_from(self.arguments_to_string_list(self.liste_noeud))
        self.DG.add_weighted_edges_from(self.attacks_to_weighted_tuple(self.liste_arc,self.weights))
        
    def strong_attacks(self):
        return [attack for attack in self.liste_arc if attack.is_strong() ]
    
    def weak_attacks(self):
        return [attack for attack in self.liste_arc if attack.is_weak() ]
    
    def beyond_any_doubt_attacks(self):
        return [attack for attack in self.liste_arc if attack.is_beyond_any_doubt() ]
    
    def stable_attacks(self):
        return self.strong_attacks() + self.beyond_any_doubt_attacks()
    
    def unstable_attacks(self):
        return self.weak_attacks()
    
    def alternative_was(self,unstable_attacks_subset):
        alWas = self.__copy__()
        for attack in unstable_attacks_subset:
                attack_index = self.liste_arc.index(attack)
                if alWas.weights[attack_index][0] != 0:
                    list_weights = list(alWas.weights[attack_index])
                    list_weights[0] = -list_weights[0]
                    alWas.weights[attack_index] = tuple(list_weights)
                    alWas.liste_arc[attack_index].edit_weight(list_weights[0])
                else:
                    list_weights = list(alWas.weights[attack_index])
                    list_weights[0] = +1
                    alWas.liste_arc[attack_index].edit_weight(+1)
                    alWas.weights[attack_index] = tuple(list_weights)
        return alWas
    
    def alternative_was_set(self):
        aws = []
        for unstable_attacks_subset in self.all_possible_sublists(self.unstable_attacks()):
            aws.append(self.alternative_was(unstable_attacks_subset))
        return aws
    
    def non_persistant_arguments(self):
        
        not_persistant_arguments_list = []
        cpwas = CounterPartAs(self)
        cpwas_in = cpwas.get_arguments_labeled_with_IN()
        cpwas_out = cpwas.get_arguments_labeled_with_OUT()
        cpwas_und = cpwas.get_arguments_labeled_with_UND()
        
        for alternative_was in self.alternative_was_set():
            
            cpalternative_was = CounterPartAs(alternative_was)
            
            cpalternative_was_in = cpalternative_was.get_arguments_labeled_with_IN()
            diff=self.difference_of_argument_list(cpwas_in,cpalternative_was_in)
            not_persistant_arguments_list.extend(x for x in diff if x not in not_persistant_arguments_list)
            
            cpalternative_was_out = cpalternative_was.get_arguments_labeled_with_OUT()
            diff=self.difference_of_argument_list(cpwas_out,cpalternative_was_out)
            not_persistant_arguments_list.extend(x for x in diff if x not in not_persistant_arguments_list)
            
            cpalternative_was_und = cpalternative_was.get_arguments_labeled_with_UND()
            diff=self.difference_of_argument_list(cpwas_und,cpalternative_was_und)
            not_persistant_arguments_list.extend(x for x in diff if x not in not_persistant_arguments_list)
            
        return not_persistant_arguments_list
         
    def persistant_arguments(self):
        return self.difference_of_argument_list(self.liste_noeud,self.non_persistant_arguments())
    
    
    def __possible_was__(self,expert,attack_name,polarity):
        was = self.__copy__()
        attack_to_update=was.liste_arc_dict[attack_name]
        Vote(attack_to_update,expert,polarity)
        was.update_weights()
        return was
    
    def possible_was_of_experts(self,experts):
        possible_was_for_experts={}
        for expert in experts:
            possible_was_s = []
            for attack_name in self.liste_arc_dict:
                was_up = self.__possible_was__(expert,attack_name,+1)
                was_down = self.__possible_was__(expert,attack_name,-1)
                possible_was_s.extend([{"attack" : attack_name , "was": was_up , "polarity" : +1},{"attack" : attack_name , "was": was_down , "polarity" : -1}])
            expert.set_possible_was(PossibleWAS(possible_was_s))
            expert_name_using_expertise= "{0}:{1}".format(expert.name,",".join(expert.expertise))
            possible_was_for_experts.update({ expert_name_using_expertise : PossibleWAS(possible_was_s)})
        return WASList(possible_was_for_experts),ExpertList(experts)

    ###### utility methods
    @staticmethod
    def attacks_to_weighted_tuple(attacks,weights):
        l = []
        i = 0
        for arc in attacks:
            l.append((str(arc.first_argument),str(arc.second_argument),weights[i][0]))
            i+=1
        return l
        
    
    def edge_labels_from_weights(self):
        str_attacks = self.attacks_to_tuple(self.liste_arc)
        labels = {}
        for i in range(0,len(self.weights)):
            s="({0},{1})".format(self.weights[i][0],self.weights[i][1])
            labels.update({ str_attacks[i] : s})
        return labels
    
    @staticmethod
    def all_possible_sublists(lst):
            # store all the sublists  
            sublist = [[]] 
            # first loop  
            for i in range(len(lst) + 1): 
            # second loop  
                for j in range(i + 1, len(lst) + 1): 
                    # slice the subarray  
                    sub = lst[i:j] 
                    sublist.append(sub)
            return sublist
        
    @staticmethod
    def difference_of_argument_list(list1,list2):
        deleted=[]
        for argument in list1:
            if argument not in list2:
                deleted.append(argument)
        return deleted
            
    
    ###### nx graph show method
    def show_graph_nx(self):
         WG=self.get_DG()
         pos = nx.random_layout(WG)
         nx.draw(WG,pos,edge_color='black',width=1,linewidths=2,\
node_size=1000,alpha=1,labels={node:node for node in WG.nodes()})
         nx.draw_networkx_edge_labels(WG,pos,edge_labels=self.edge_labels_from_weights(), label_pos=0.5)
         