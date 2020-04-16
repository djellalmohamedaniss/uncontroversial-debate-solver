import json
from Expert import Expert
from Argument import Argument
from Attack import Attack

def fillArgumentsAndExperts(JSON):
    arguments_list = {}
    experts_list = {}
    for expert, properties in JSON.items():
       arguments = properties.items()
       expert_arguments = {}
       expert_expertise = []
       for argument, ar_properties in arguments:
           arg = Argument(argument,ar_properties['top'],ar_properties['attacks'])
           expert_arguments.update({argument: arg})
           expert_expertise.extend(ar_properties['top'])
       arguments_list.update(expert_arguments)
       expert_object = Expert(expert,expert_arguments,expert_expertise)   
       experts_list.update({expert : expert_object})
    return arguments_list,experts_list

def fillAttacks(JSON,arguments):
     attacks_list = {}
     for expert, properties in JSON.items():
       for argument, ar_properties in properties.items():
           for attacking in ar_properties['attacks']:
               attack = Attack(arguments[argument],arguments[attacking])
               attack_key = "{0}=>{1}".format(argument,attacking)
               attacks_list.update({attack_key : attack})
     return attacks_list
            


def read_schema():
    with open('schema.json') as json_data:
        schema = json.load(json_data)
        arguments,experts = fillArgumentsAndExperts(schema['experts'])
        attacks = fillAttacks(schema["experts"],arguments)
    return arguments,experts,attacks

