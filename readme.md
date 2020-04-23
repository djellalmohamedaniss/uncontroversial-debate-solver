# uncontroversial-debate-solver

this is a school project on argumentation systems, where our goal is to pick the right expert to make a debate uncontroversial. The paper can be found [here](http://helios.mi.parisdescartes.fr/~moraitis/webpapers/Moraitis-COMMA12b.pdf)

## Installation

After downloading the project, open the terminal in the root of your project and follow this [tutorial](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). At the end, your virtual python environment will be set to install the following libraries: 

the library [networkx](https://networkx.github.io/) is used to manipulate and create directed graphs.

```bash
pip install networkx
```

the library [prettytable](https://github.com/jazzband/prettytable) is used to print tables on console.

```bash
pip3 install PTable
```

the library [termcolor](https://pypi.org/project/termcolor/) is used to color text, make it bold, etc....

```bash
pip install termcolor
```

## Usage

```python
python3 Main.py "path/to/your/schema.json"
```

## Argumentation system file schema
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

## to-do list

- [ ] Refactor the project into folders.
- [ ] Adding natural text parser.
- [ ] Create a GUI.
