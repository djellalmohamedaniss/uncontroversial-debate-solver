from Vote import Vote
from WAS import WAS
from ExpertWithWAS import ExpertWithWAS as Expert
import Parser

def main():
    
    arguments,experts,attacks,topics=Parser.read_schema()

    # votes
    vote12 = Vote(attacks['b,a'], experts['PC2'], 1)
    vote22 = Vote(attacks['b,a'], experts['PC3'], -1)
    vote32 = Vote(attacks['b,a'], experts['PC1'], -1)
    vote11 = Vote(attacks['c,b'], experts['PC2'], 1)
    vote21 = Vote(attacks['c,b'], experts['PC3'], 1)
    vote31 = Vote(attacks['c,b'], experts['PC1'], -1)
    vote13 = Vote(attacks['d,a'], experts['PC2'], 1)
    
    attacks['c,b'].apply_votes([vote11, vote21, vote31])
    attacks['b,a'].apply_votes([vote12, vote22, vote32])
    attacks['d,a'].apply_votes([vote13])
    
    was=WAS(arguments,attacks)
    pws,experts=was.possible_was_of_experts(Expert.__generator__(topics,expertise_cardinal=2))

    print(pws.table_possible_was())
    
    for exp in experts:
        for expert in experts:
            if exp.necessarily_dominate(expert) and exp != expert:
                print(exp.name,expert.name)
    
    

if __name__ == "__main__":
    main()
