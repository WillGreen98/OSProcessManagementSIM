from enum import Enum


class ALGORITHM(Enum):
    FCFS = 0
    SJF = 1
    PRIORITY = 2
    ROUND_ROBIN = 3

class STATE(Enum):
    PROCESSING = 0
    TERMINATED = 1
    WAITING = 2

class CPU_MODE(Enum):
    INTERRUPT = 0
    FIXED_CYCLE = 1

