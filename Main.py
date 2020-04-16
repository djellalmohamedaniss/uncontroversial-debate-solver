from Vote import Vote
from WAS import WAS
import Parser
import pprint


def main():
    pp = pprint.PrettyPrinter(indent=4,width=80)
    arguments,experts,attacks=Parser.read_schema()
    vote12 = Vote(attacks['b=>a'], experts['PC2'], 1)
    vote22 = Vote(attacks['b=>a'], experts['PC3'], -1)
    vote32 = Vote(attacks['b=>a'], experts['PC1'], -1)
    vote11 = Vote(attacks['c=>b'], experts['PC2'], 1)
    vote21 = Vote(attacks['c=>b'], experts['PC3'], 1)
    vote31 = Vote(attacks['c=>b'], experts['PC1'], -1)
    vote13 = Vote(attacks['d=>a'], experts['PC2'], 1)
    attacks['c=>b'].apply_votes([vote11, vote21, vote31])
    attacks['b=>a'].apply_votes([vote12, vote22, vote32])
    attacks['d=>a'].apply_votes([vote13])
    was1=WAS(list(arguments.values()),list(attacks.values()))
    pp.pprint(was1)
    pp.pprint(was1.persistant_arguments())
    pp.pprint(was1.non_persistant_arguments())

    
    
    
    
    

if __name__ == "__main__":
    main()
