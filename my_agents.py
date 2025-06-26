# my_agents.py

class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

class Runner:
    @staticmethod
    def run_sync(agent, prompt):
        # Simple response example
        response = f"{agent.name} says: I am fine, thank you! (You said: {prompt})"
        return type('Response', (object,), {'final_output': response})()

