from WAS import WAS
from ExpertWithWAS import ExpertWithWAS as Expert
import WASFileParser as WFP
import sys


def main():
    
    try:
        filename = sys.argv[1]
    except IndexError:
        print("ERROR! No file passed as first argument")
        return 0
    
    arguments,attacks,topics = WFP.read(filename)
    
    was=WAS(arguments,attacks)
    
    pws,experts=was.possible_was_of_experts(Expert.__generator__(topics,expertise_cardinal=2))

    print("\nconsequences of every potential expert vote\n")

    print(pws.table_possible_was())
    
    print("\nbest experts to pick are:\n\n{0}".format(experts.best()))
    
    
if __name__ == "__main__":
    main()