from Expert import Expert
from Argument import Argument
from Attack import Attack
from Vote import Vote
from WAS import WAS

def main():
    
    c = Argument('c', ['comp', 'ml'], {'b'})
    b = Argument('b', ['comp'], {})
    d = Argument('d', ['kr'], {'a'})
    a = Argument('a', ['kr', 'cog'], {})
    PC1 = Expert("PC1", [a], ['kr', 'cog'])
    PC2 = Expert("PC2", [d, b], ['kr', 'comp'])
    PC3 = Expert("PC3", [c], ['ml', 'comp'])
    att1 = Attack(c, b)
    att2 = Attack(b, a)
    att3 = Attack(d, a)
    vote12 = Vote(att2, PC2, 1)
    vote22 = Vote(att2, PC3, -1)
    vote32 = Vote(att2, PC1, -1)
    vote11 = Vote(att1, PC2, 1)
    vote21 = Vote(att1, PC3, 1)
    vote31 = Vote(att1, PC1, -1)
    vote13 = Vote(att3, PC2, 1)
    att1.apply_votes([vote11, vote21, vote31])
    att2.apply_votes([vote12, vote22, vote32])
    att3.apply_votes([vote13])
    
    was1=WAS([a,b,c,d],[att1,att2,att3])
    print(was1.persistant_arguments())
    print(was1.non_persistant_arguments())
    

if __name__ == "__main__":
    main()
