class Automaton(object):

    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endState = None
        
    def add_state(self, name, handler):
        name = name.upper()
        self.handlers[name] = handler
        
    def set_start(self, name):
        self.startState = name.upper()
    
    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            print("Must initialize a start state")
        for command in cargo:
            (newState, cargo) = handler(command)
            handler = self.handlers[newState.upper()]
        return newState
    
    def read_commands(self, commands):
    # Return True if we end in our accept state, False otherwise
        my_automaton.add_state("q1", q1_transitions)
        my_automaton.add_state("q2", q2_transitions)
        my_automaton.add_state("q3", q3_transitions)
        my_automaton.set_start("q1")
        self.endState = my_automaton.run(commands)
        return self.endState == "q2"

def q1_transitions(txt):
    if txt == "1":
        newState = "q2"
    else:
        newState = "q1"
    return (newState, txt)
    
def q2_transitions(txt):
    if txt == "1":
        newState = "q2"
    else:
        newState = "q3"
    return (newState, txt)

def q3_transitions(txt):
    newState = "q2"
    return (newState, txt)

my_automaton = Automaton()