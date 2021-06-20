import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass

class Job:
    def __init__(self, task_id, deadline, profit) -> None:
        self.task_id = task_id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs, T):
    profit = 0
    slot = [-1] * T # each index corresponds to one deadline

    jobs.sort(key=lambda x: x.profit, reverse=True)

    for job in jobs:
        for j in reversed(range(job.deadline)):
            if j < T and slot[j] == -1:
                slot[j] = job.task_id
                profit += job.profit
                break
    
    return ([i for i in slot if i != -1], profit)

jobs = [
        Job(1, 9, 15), Job(2, 2, 2),
        Job(3, 5, 18), Job(4, 7, 1),
        Job(5, 4, 25), Job(6, 2, 20),
        Job(7, 5, 8), Job(8, 7, 10),
        Job(9, 4, 12), Job(10, 3, 5)
    ]

T = 15 # maximum deadline

slot, profit = job_sequencing(jobs, T)
print('Slot: ', slot)
print('Profit: ', profit)
