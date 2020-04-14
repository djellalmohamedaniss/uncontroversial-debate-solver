class Argument:
    def __init__(self, name, topics, challenges):
        self.name = name
        self.topics = topics
        self.challenges = challenges
        
    def __eq__(self,obj):
        return self.name == obj.name 
    
    def __hash__(self):
        hash((self.name, self.topics, self.challenges))

    def __repr__(self):
        return self.name

    def top(self):
        return self.topics
