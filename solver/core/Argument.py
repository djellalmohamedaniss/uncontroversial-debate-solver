class Argument:
    def __init__(self, name, topics, challenges):
        self.name = name
        self.topics = topics
        self.challenges = challenges
        
    def __eq__(self,obj):
        return self.name == obj.name 
    
    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return "<{0}>".format(self.name)

    def top(self):
        return self.topics