# Picking the Right Expert to Make a Debate Uncontroversial

this is a school project on argumentation systems, where the goal is to implement a solver to pick the right expert that makes a debate uncontroversial. The paper can be found [here](http://helios.mi.parisdescartes.fr/~moraitis/webpapers/Moraitis-COMMA12b.pdf)

## Abstract

Agents contributing to (online) debate systems often have different areas of expertise. This must be considered if we want to define a decision making process based on the output of such a system. Distinguishing agents on the basis of their areas of expertise also opens an interesting perspective: when a debate is deemed 'controversial', calling an additional expert may be a natural way to make the decision easier. We introduce possible definitions that capture these notions and we provide a preliminary analysis with the objective to help a designer find the 'right' expert.

## Usage

```
main.py [-h] --data FILENAME [--verbose] [--output [OUTPUT_PATH]]

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         show the 'WAS table' and detailed prints
  --output [OUTPUT_PATH], -o [OUTPUT_PATH]
                        the directory of the file where the result is stored,
                        default is the current path

required arguments:
  --data FILENAME, -d FILENAME
                        the path to the schema json file
```

## Argumentation system input file schema
The schema of the argumentation system is stored is a JSON file with the following tree:


```json
"experts" : {
  "expert_name" : {
     "arguments" : {
        "argument_name" : {
           "attacks" : ,
           "top" 
        }
     },
     "votes" : {
      "vote_index" : {
         "argument" : , 
         "target" : ,
         "polarity"
      }
     }
  }
}
```

## Citation

```
@inproceedings{inproceedings,
author = {Kontarinis, Dionysios and Bonzon, Elise and Maudet, Nicolas and Moraitis, Pavlos},
year = {2012},
month = {09},
pages = {486-497},
title = {Picking the Right Expert to Make a Debate Uncontroversial},
volume = {245},
journal = {Frontiers in Artificial Intelligence and Applications},
doi = {10.3233/978-1-61499-111-3-486}
}
```

## To-do list

- [ ] Refactor the project into folders.
- [ ] Adding natural text parser.
- [ ] Create a GUI.
