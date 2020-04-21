from Vote import Vote
from WAS import WAS
from ExpertWithWAS import ExpertWithWAS as Expert
import Parser
from networkx import networkx as nx


def main():
    
    arguments,experts,attacks,topics=Parser.read_schema()

    # votes
    Vote(attacks['b,a'], experts['PC2'], 1)
    Vote(attacks['b,a'], experts['PC3'], -1)
    Vote(attacks['b,a'], experts['PC1'], -1)
    Vote(attacks['c,b'], experts['PC2'], 1)
    Vote(attacks['c,b'], experts['PC3'], 1)
    Vote(attacks['c,b'], experts['PC1'], -1)
    Vote(attacks['d,a'], experts['PC2'], 1)
    
    was=WAS(arguments,attacks)
    pws,experts=was.possible_was_of_experts(Expert.__generator__(topics,expertise_cardinal=2))

    print(pws.table_possible_was())
    
    print(experts.best())
    

if __name__ == "__main__":
    main()
