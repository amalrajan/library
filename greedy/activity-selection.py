import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def activity_selection(start, finish, n):
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if finish[j] < finish[mini]:
                mini = j
        
        if i != mini:
            finish[i], finish[mini] = finish[mini], finish[i]
            start[i], start[mini] = start[mini], start[i]

    schedule = [(start[0], finish[0])]

    k = 0
    for i in range(1, n):
        if start[i] >= finish[k]:
            schedule.append((start[i], finish[i]))
            k = i

    return schedule

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
n = len(start)

schedule = activity_selection(start, finish, n)

for i in schedule:
    print(i)
