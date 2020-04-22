import json
from Expert import Expert
from Argument import Argument
from Attack import Attack
from Vote import Vote

def fillArgumentsAndExperts(JSON):
    arguments_list = {}
    experts_list = {}
    topics_list = []
    for expert, properties in JSON.items():
       data = properties['arguments'].items()
       expert_arguments = {}
       expert_expertise = []
       for argument, ar_properties in data:
           arg = Argument(argument,ar_properties['top'],ar_properties['attacks'])
           expert_arguments.update({argument: arg})
           expert_expertise.extend(ar_properties['top'])
           topics_list.extend(ar_properties['top'])
       arguments_list.update(expert_arguments)
       expert_object = Expert(expert,expert_arguments,expert_expertise)   
       experts_list.update({expert : expert_object})
    return arguments_list,experts_list,set(topics_list)

def fillAttacks(JSON,arguments,topics):
     attacks_list = {}
     for expert, properties in JSON.items():
       for argument, ar_properties in properties['arguments'].items():
           for attacking in ar_properties['attacks']:
               attack = Attack(arguments[argument],arguments[attacking],topics)
               attack_key = "{0},{1}".format(argument,attacking)
               attacks_list.update({attack_key : attack})
     return attacks_list
 

def fillVotes(JSON,attacks,experts):
    for expert, properties in JSON.items():
       for index, vote_properties in properties['votes'].items():
               attack_index = "{0},{1}".format(vote_properties["argument"],vote_properties["target"])
               Vote(attacks[attack_index], experts[expert], vote_properties["polarity"])
               
           
            


def read(filename):
    with open(filename) as json_data:
        schema = json.load(json_data)
        arguments,experts,topics = fillArgumentsAndExperts(schema['experts'])
        attacks = fillAttacks(schema["experts"],arguments,topics)
        fillVotes(schema["experts"],attacks,experts)
    return arguments,attacks,topics
