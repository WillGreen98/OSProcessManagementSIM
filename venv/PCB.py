import time
from GLOBALS import ALGORITHM, STATE, CPU_MODE
from prettytable import PrettyTable

DEFAULT_CPU_CYLE = 23

class PCB():
    def __init__(self, name, id, priority,state, job_length ):
        self.name = name
        self.id = id
        self.priority = priority
        self.state = state
        self.job_length = job_length

    def add_me_to_print(self,t = None):
        if t is None:
            pass
        else:
            t.add_row([self.id, self.name, self.priority,self.state,self.job_length])


