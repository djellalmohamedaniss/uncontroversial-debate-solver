from itertools import combinations


class Expert:

    def __init__(self, name, arguments, expertise):
        self.name = name
        self.arguments = arguments
        self.expertise = expertise

    def __repr__(self):
        return "expert <{0}> with expertise in {1} has the set of arguments => {2}".format(self.name, self.expertise,
                                                                                           self.arguments)

    def __eq__(self, expert):
        return self.name == expert.name and self.expertise == expert.expertise

    def __ne__(self, expert):
        return not self.__eq__(expert)

    def impact(self, attack):
        inter_prom = []
        inter_rel = []
        imp = 0
        liste_expertises = self.expertise
        inter_prom = self.intersection(liste_expertises, attack.prominent())
        inter_rel = self.intersection(liste_expertises, attack.relevant())
        imp = 2 * len(inter_prom) + len(inter_rel)
        return imp

    @staticmethod
    def intersection(lst1, lst2):
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return lst3

    @staticmethod
    def __generator__(topics, expertise_cardinal):
        experts = []
        combins = [list(comb) for comb in combinations(topics, expertise_cardinal)]
        for combin in combins:
            expert = Expert("EX{0}".format(combin), [], combin)
            experts.append(expert)
        return experts
