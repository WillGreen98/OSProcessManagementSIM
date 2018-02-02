import time
import os
from GLOBALS import ALGORITHM, STATE, CPU_MODE
from prettytable import PrettyTable
from PCB import PCB

DEFAULT_CPU_CYCLE = 23


class QueueManager():
    def __init__(self):
        self.queue = []
        self.processes_switches = 0

    def add_process(self, pcb):
        self.queue.append(pcb)

    def print_queue(self):
        self.t = PrettyTable(['ID', 'Name', 'Priority', "State", "job Length"])
        for pcb in self.queue:
            pcb.add_me_to_print(self.t)
        print(self.t)

    def implement_algorithm(self, alg ):
        if alg == ALGORITHM.FCFS:
            self.FCFS(CPU_MODE.INTERRUPT)
        elif alg == ALGORITHM.SJF:
            pass
        elif alg == ALGORITHM.PRIORITY:
            pass
        elif alg == ALGORITHM.ROUND_ROBIN:
            self.ROUND_ROBIN(CPU_MODE.FIXED_CYCLE,False)

    def FCFS(self,cpu_mode):
        for pcb in self.queue:
            self.process_switch_overhead()
            cpu_cycles = pcb.job_length
            for i in range(cpu_cycles):
                pcb.job_length -= 1
                pcb .state = STATE.PROCESSING
                self.print_queue()
                self.fetch_execute_overhead()
                if pcb.job_length <=0:
                     pcb.state = STATE.TERMINATED
                     self.print_queue()

    def ROUND_ROBIN(self,cpu_mode, queue_processed):
        if queue_processed:
            return
        processed_flag = True
        queue = list(reversed(self.queue))
        for pcb in queue:
            self.process_switch_overhead()
            if pcb.state != STATE.TERMINATED and pcb.job_length >0:
                for i in range(DEFAULT_CPU_CYCLE):
                    processed_flag = False
                    pcb.state = STATE.PROCESSING
                    pcb.job_length -= 1
                    self.print_queue()
                    self.fetch_execute_overhead()
                    if pcb.job_length <=0:
                         pcb.state = STATE.TERMINATED
                         break
                         #self.print_queue()
            if pcb.state != STATE.TERMINATED:
                pcb.state = STATE.WAITING

        self.ROUND_ROBIN(cpu_mode,processed_flag)

    def process_switch_overhead(self):
        time.sleep(1)
        #print("Process Switch")
        self.process_switches += 1

    def fetch_execute_overhead(self):
        time.sleep(.5)
        #print("Fetch-Execute Cycle")