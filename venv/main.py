import time
from GLOBALS import ALGORITHM, STATE
from Scheduler import PCB, QueueManager
from enum import Enum



def init_scheduler():
    q = QueueManager()
    q.add_process(PCB("Augmented Browser","AB", 34,STATE.WAITING,72))
    q.add_process(PCB("Augmented Media Player","AMP", 56,STATE.WAITING,45))
    q.add_process(PCB("Augmented Doc Tool","ADT", 23,STATE.WAITING,33))
    q.print_queue()
    q.process_switches = 0
    return q


q = init_scheduler()


#q.implement_algorithm(ALGORITHM.FCFS)   #1m17s89
q.implement_algorithm(ALGORITHM.ROUND_ROBIN)   #1m 29s 71


#######################
q.print_queue()
print("process Switches: ", q.process_switches)


