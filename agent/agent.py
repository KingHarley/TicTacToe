import random

class agent:
    def __init__(self, type):
        if(type == "random"):
            self.agent = randomAgent()
        else:
            self.agent = randomAgent()
    
    def step(self, actionspace):
        return self.agent.step(actionspace)


class randomAgent:
    def step(self, actionspace):
        return random.choice(actionspace)
    
    
        